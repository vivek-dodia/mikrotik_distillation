# Repository Information
Name: mikrotik-rif-viewer

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/irrwitzer42/mikrotik-rif-viewer.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
image: docker.io/node:20-alpine3.19
pages:
  script:
    - npm install
    - npm run build
    - rm -rf public
    - mv dist public
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
================================================

File: docker-compose.yml
================================================
services:
  mikrotik-rif-viewer:
    #image: mikrotik-rif-viewer:latest
    build: .
    container_name: rif-viewer
    restart: unless-stopped
    ports:
      - 4242:4173
================================================

File: Dockerfile
================================================
FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN sed -ie 's%"preview": "vite preview"$%"preview": "vite preview --host"%g' package.json
RUN npm run build
EXPOSE 4173
CMD [ "npm", "run", "preview" ]
================================================

File: index.html
================================================
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mikrotik RIF Viewer</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
================================================

File: package-lock.json
================================================
{
  "name": "mikrotik-rif-viewer",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "mikrotik-rif-viewer",
      "version": "0.0.0",
      "dependencies": {
        "@highlightjs/vue-plugin": "^2.1.0",
        "highlight.js": "^11.9.0",
        "pako": "^2.1.0",
        "primeflex": "^3.3.1",
        "primeicons": "^6.0.1",
        "primevue": "^3.49.1",
        "vue": "^3.4.19"
      },
      "devDependencies": {
        "@types/pako": "^2.0.3",
        "@vitejs/plugin-vue": "^5.0.4",
        "typescript": "^5.2.2",
        "vite": "^5.1.4",
        "vue-tsc": "^1.8.27"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.24.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.24.0.tgz",
      "integrity": "sha512-QuP/FxEAzMSjXygs8v4N9dvdXzEHN4W1oF3PxuWAtPo08UdM17u89RDMgjLn/mlc56iM0HlLmVkO/wgR+rDgHg==",
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.19.12.tgz",
      "integrity": "sha512-bmoCYyWdEL3wDQIVbcyzRyeKLgk2WtWLTWz1ZIAZF/EGbNOwSA6ew3PftJ1PqMiOOGu0OyFMzG53L0zqIpPeNA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.19.12.tgz",
      "integrity": "sha512-qg/Lj1mu3CdQlDEEiWrlC4eaPZ1KztwGJ9B6J+/6G+/4ewxJg7gqj8eVYWvao1bXrqGiW2rsBZFSX3q2lcW05w==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.19.12.tgz",
      "integrity": "sha512-P0UVNGIienjZv3f5zq0DP3Nt2IE/3plFzuaS96vihvD0Hd6H/q4WXUGpCxD/E8YrSXfNyRPbpTq+T8ZQioSuPA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.19.12.tgz",
      "integrity": "sha512-3k7ZoUW6Q6YqhdhIaq/WZ7HwBpnFBlW905Fa4s4qWJyiNOgT1dOqDiVAQFwBH7gBRZr17gLrlFCRzF6jFh7Kew==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.19.12.tgz",
      "integrity": "sha512-B6IeSgZgtEzGC42jsI+YYu9Z3HKRxp8ZT3cqhvliEHovq8HSX2YX8lNocDn79gCKJXOSaEot9MVYky7AKjCs8g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.19.12.tgz",
      "integrity": "sha512-hKoVkKzFiToTgn+41qGhsUJXFlIjxI/jSYeZf3ugemDYZldIXIxhvwN6erJGlX4t5h417iFuheZ7l+YVn05N3A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.19.12.tgz",
      "integrity": "sha512-4aRvFIXmwAcDBw9AueDQ2YnGmz5L6obe5kmPT8Vd+/+x/JMVKCgdcRwH6APrbpNXsPz+K653Qg8HB/oXvXVukA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.19.12.tgz",
      "integrity": "sha512-EYoXZ4d8xtBoVN7CEwWY2IN4ho76xjYXqSXMNccFSx2lgqOG/1TBPW0yPx1bJZk94qu3tX0fycJeeQsKovA8gg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.19.12.tgz",
      "integrity": "sha512-J5jPms//KhSNv+LO1S1TX1UWp1ucM6N6XuL6ITdKWElCu8wXP72l9MM0zDTzzeikVyqFE6U8YAV9/tFyj0ti+w==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.19.12.tgz",
      "integrity": "sha512-EoTjyYyLuVPfdPLsGVVVC8a0p1BFFvtpQDB/YLEhaXyf/5bczaGeN15QkR+O4S5LeJ92Tqotve7i1jn35qwvdA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.19.12.tgz",
      "integrity": "sha512-Thsa42rrP1+UIGaWz47uydHSBOgTUnwBwNq59khgIwktK6x60Hivfbux9iNR0eHCHzOLjLMLfUMLCypBkZXMHA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.19.12.tgz",
      "integrity": "sha512-LiXdXA0s3IqRRjm6rV6XaWATScKAXjI4R4LoDlvO7+yQqFdlr1Bax62sRwkVvRIrwXxvtYEHHI4dm50jAXkuAA==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.19.12.tgz",
      "integrity": "sha512-fEnAuj5VGTanfJ07ff0gOA6IPsvrVHLVb6Lyd1g2/ed67oU1eFzL0r9WL7ZzscD+/N6i3dWumGE1Un4f7Amf+w==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.19.12.tgz",
      "integrity": "sha512-nYJA2/QPimDQOh1rKWedNOe3Gfc8PabU7HT3iXWtNUbRzXS9+vgB0Fjaqr//XNbd82mCxHzik2qotuI89cfixg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.19.12.tgz",
      "integrity": "sha512-2MueBrlPQCw5dVJJpQdUYgeqIzDQgw3QtiAHUC4RBz9FXPrskyyU3VI1hw7C0BSKB9OduwSJ79FTCqtGMWqJHg==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.19.12.tgz",
      "integrity": "sha512-+Pil1Nv3Umes4m3AZKqA2anfhJiVmNCYkPchwFJNEJN5QxmTs1uzyy4TvmDrCRNT2ApwSari7ZIgrPeUx4UZDg==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.19.12.tgz",
      "integrity": "sha512-B71g1QpxfwBvNrfyJdVDexenDIt1CiDN1TIXLbhOw0KhJzE78KIFGX6OJ9MrtC0oOqMWf+0xop4qEU8JrJTwCg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.19.12.tgz",
      "integrity": "sha512-3ltjQ7n1owJgFbuC61Oj++XhtzmymoCihNFgT84UAmJnxJfm4sYCiSLTXZtE00VWYpPMYc+ZQmB6xbSdVh0JWA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.19.12.tgz",
      "integrity": "sha512-RbrfTB9SWsr0kWmb9srfF+L933uMDdu9BIzdA7os2t0TXhCRjrQyCeOt6wVxr79CKD4c+p+YhCj31HBkYcXebw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.19.12.tgz",
      "integrity": "sha512-HKjJwRrW8uWtCQnQOz9qcU3mUZhTUQvi56Q8DPTLLB+DawoiQdjsYq+j+D3s9I8VFtDr+F9CjgXKKC4ss89IeA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.19.12.tgz",
      "integrity": "sha512-URgtR1dJnmGvX864pn1B2YUYNzjmXkuJOIqG2HdU62MVS4EHpU2946OZoTMnRUHklGtJdJZ33QfzdjGACXhn1A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.19.12.tgz",
      "integrity": "sha512-+ZOE6pUkMOJfmxmBZElNOx72NKpIa/HFOMGzu8fqzQJ5kgf6aTGrcJaFsNiVMH4JKpMipyK+7k0n2UXN7a8YKQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.19.12.tgz",
      "integrity": "sha512-T1QyPSDCyMXaO3pzBkF96E8xMkiRYbUEZADd29SyPGabqxMViNoii+NcK7eWJAEoU6RZyEm5lVSIjTmcdoB9HA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@highlightjs/vue-plugin": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@highlightjs/vue-plugin/-/vue-plugin-2.1.0.tgz",
      "integrity": "sha512-E+bmk4ncca+hBEYRV2a+1aIzIV0VSY/e5ArjpuSN9IO7wBJrzUE2u4ESCwrbQD7sAy+jWQjkV5qCCWgc+pu7CQ==",
      "peerDependencies": {
        "highlight.js": "^11.0.1",
        "vue": "^3"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.4.15",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.4.15.tgz",
      "integrity": "sha512-eF2rxCRulEKXHTRiDrDy6erMYWqNw4LPdQ8UQA4huuxaQsVeRPFl2oM8oDGxMFhJUWZf9McpLtJasDDZb/Bpeg=="
    },
    "node_modules/@rollup/rollup-android-arm-eabi": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.12.1.tgz",
      "integrity": "sha512-iU2Sya8hNn1LhsYyf0N+L4Gf9Qc+9eBTJJJsaOGUp+7x4n2M9dxTt8UvhJl3oeftSjblSlpCfvjA/IfP3g5VjQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-android-arm64": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.12.1.tgz",
      "integrity": "sha512-wlzcWiH2Ir7rdMELxFE5vuM7D6TsOcJ2Yw0c3vaBR3VOsJFVTx9xvwnAvhgU5Ii8Gd6+I11qNHwndDscIm0HXg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-darwin-arm64": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.12.1.tgz",
      "integrity": "sha512-YRXa1+aZIFN5BaImK+84B3uNK8C6+ynKLPgvn29X9s0LTVCByp54TB7tdSMHDR7GTV39bz1lOmlLDuedgTwwHg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-darwin-x64": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.12.1.tgz",
      "integrity": "sha512-opjWJ4MevxeA8FhlngQWPBOvVWYNPFkq6/25rGgG+KOy0r8clYwL1CFd+PGwRqqMFVQ4/Qd3sQu5t7ucP7C/Uw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.12.1.tgz",
      "integrity": "sha512-uBkwaI+gBUlIe+EfbNnY5xNyXuhZbDSx2nzzW8tRMjUmpScd6lCQYKY2V9BATHtv5Ef2OBq6SChEP8h+/cxifQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-gnu": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.12.1.tgz",
      "integrity": "sha512-0bK9aG1kIg0Su7OcFTlexkVeNZ5IzEsnz1ept87a0TUgZ6HplSgkJAnFpEVRW7GRcikT4GlPV0pbtVedOaXHQQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-musl": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.12.1.tgz",
      "integrity": "sha512-qB6AFRXuP8bdkBI4D7UPUbE7OQf7u5OL+R94JE42Z2Qjmyj74FtDdLGeriRyBDhm4rQSvqAGCGC01b8Fu2LthQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-gnu": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.12.1.tgz",
      "integrity": "sha512-sHig3LaGlpNgDj5o8uPEoGs98RII8HpNIqFtAI8/pYABO8i0nb1QzT0JDoXF/pxzqO+FkxvwkHZo9k0NJYDedg==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-gnu": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.12.1.tgz",
      "integrity": "sha512-nD3YcUv6jBJbBNFvSbp0IV66+ba/1teuBcu+fBBPZ33sidxitc6ErhON3JNavaH8HlswhWMC3s5rgZpM4MtPqQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-musl": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.12.1.tgz",
      "integrity": "sha512-7/XVZqgBby2qp/cO0TQ8uJK+9xnSdJ9ct6gSDdEr4MfABrjTyrW6Bau7HQ73a2a5tPB7hno49A0y1jhWGDN9OQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-win32-arm64-msvc": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.12.1.tgz",
      "integrity": "sha512-CYc64bnICG42UPL7TrhIwsJW4QcKkIt9gGlj21gq3VV0LL6XNb1yAdHVp1pIi9gkts9gGcT3OfUYHjGP7ETAiw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-ia32-msvc": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.12.1.tgz",
      "integrity": "sha512-LN+vnlZ9g0qlHGlS920GR4zFCqAwbv2lULrR29yGaWP9u7wF5L7GqWu9Ah6/kFZPXPUkpdZwd//TNR+9XC9hvA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-msvc": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.12.1.tgz",
      "integrity": "sha512-n+vkrSyphvmU0qkQ6QBNXCGr2mKjhP08mPRM/Xp5Ck2FV4NrHU+y6axzDeixUrCBHVUS51TZhjqrKBBsHLKb2Q==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@types/estree": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.5.tgz",
      "integrity": "sha512-/kYRxGDLWzHOB7q+wtSUQlFrtcdUccpfy+X+9iMBpHK8QLLhx2wIPYuS5DYtR9Wa/YlZAbIovy7qVdB1Aq6Lyw==",
      "dev": true
    },
    "node_modules/@types/pako": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/@types/pako/-/pako-2.0.3.tgz",
      "integrity": "sha512-bq0hMV9opAcrmE0Byyo0fY3Ew4tgOevJmQ9grUhpXQhYfyLJ1Kqg3P33JT5fdbT2AjeAjR51zqqVjAL/HMkx7Q==",
      "dev": true
    },
    "node_modules/@vitejs/plugin-vue": {
      "version": "5.0.4",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-vue/-/plugin-vue-5.0.4.tgz",
      "integrity": "sha512-WS3hevEszI6CEVEx28F8RjTX97k3KsrcY6kvTg7+Whm5y3oYvcqzVeGCU3hxSAn4uY2CLCkeokkGKpoctccilQ==",
      "dev": true,
      "engines": {
        "node": "^18.0.0 || >=20.0.0"
      },
      "peerDependencies": {
        "vite": "^5.0.0",
        "vue": "^3.2.25"
      }
    },
    "node_modules/@volar/language-core": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@volar/language-core/-/language-core-1.11.1.tgz",
      "integrity": "sha512-dOcNn3i9GgZAcJt43wuaEykSluAuOkQgzni1cuxLxTV0nJKanQztp7FxyswdRILaKH+P2XZMPRp2S4MV/pElCw==",
      "dev": true,
      "dependencies": {
        "@volar/source-map": "1.11.1"
      }
    },
    "node_modules/@volar/source-map": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@volar/source-map/-/source-map-1.11.1.tgz",
      "integrity": "sha512-hJnOnwZ4+WT5iupLRnuzbULZ42L7BWWPMmruzwtLhJfpDVoZLjNBxHDi2sY2bgZXCKlpU5XcsMFoYrsQmPhfZg==",
      "dev": true,
      "dependencies": {
        "muggle-string": "^0.3.1"
      }
    },
    "node_modules/@volar/typescript": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@volar/typescript/-/typescript-1.11.1.tgz",
      "integrity": "sha512-iU+t2mas/4lYierSnoFOeRFQUhAEMgsFuQxoxvwn5EdQopw43j+J27a4lt9LMInx1gLJBC6qL14WYGlgymaSMQ==",
      "dev": true,
      "dependencies": {
        "@volar/language-core": "1.11.1",
        "path-browserify": "^1.0.1"
      }
    },
    "node_modules/@vue/compiler-core": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/compiler-core/-/compiler-core-3.4.21.tgz",
      "integrity": "sha512-MjXawxZf2SbZszLPYxaFCjxfibYrzr3eYbKxwpLR9EQN+oaziSu3qKVbwBERj1IFIB8OLUewxB5m/BFzi613og==",
      "dependencies": {
        "@babel/parser": "^7.23.9",
        "@vue/shared": "3.4.21",
        "entities": "^4.5.0",
        "estree-walker": "^2.0.2",
        "source-map-js": "^1.0.2"
      }
    },
    "node_modules/@vue/compiler-dom": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/compiler-dom/-/compiler-dom-3.4.21.tgz",
      "integrity": "sha512-IZC6FKowtT1sl0CR5DpXSiEB5ayw75oT2bma1BEhV7RRR1+cfwLrxc2Z8Zq/RGFzJ8w5r9QtCOvTjQgdn0IKmA==",
      "dependencies": {
        "@vue/compiler-core": "3.4.21",
        "@vue/shared": "3.4.21"
      }
    },
    "node_modules/@vue/compiler-sfc": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/compiler-sfc/-/compiler-sfc-3.4.21.tgz",
      "integrity": "sha512-me7epoTxYlY+2CUM7hy9PCDdpMPfIwrOvAXud2Upk10g4YLv9UBW7kL798TvMeDhPthkZ0CONNrK2GoeI1ODiQ==",
      "dependencies": {
        "@babel/parser": "^7.23.9",
        "@vue/compiler-core": "3.4.21",
        "@vue/compiler-dom": "3.4.21",
        "@vue/compiler-ssr": "3.4.21",
        "@vue/shared": "3.4.21",
        "estree-walker": "^2.0.2",
        "magic-string": "^0.30.7",
        "postcss": "^8.4.35",
        "source-map-js": "^1.0.2"
      }
    },
    "node_modules/@vue/compiler-ssr": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/compiler-ssr/-/compiler-ssr-3.4.21.tgz",
      "integrity": "sha512-M5+9nI2lPpAsgXOGQobnIueVqc9sisBFexh5yMIMRAPYLa7+5wEJs8iqOZc1WAa9WQbx9GR2twgznU8LTIiZ4Q==",
      "dependencies": {
        "@vue/compiler-dom": "3.4.21",
        "@vue/shared": "3.4.21"
      }
    },
    "node_modules/@vue/language-core": {
      "version": "1.8.27",
      "resolved": "https://registry.npmjs.org/@vue/language-core/-/language-core-1.8.27.tgz",
      "integrity": "sha512-L8Kc27VdQserNaCUNiSFdDl9LWT24ly8Hpwf1ECy3aFb9m6bDhBGQYOujDm21N7EW3moKIOKEanQwe1q5BK+mA==",
      "dev": true,
      "dependencies": {
        "@volar/language-core": "~1.11.1",
        "@volar/source-map": "~1.11.1",
        "@vue/compiler-dom": "^3.3.0",
        "@vue/shared": "^3.3.0",
        "computeds": "^0.0.1",
        "minimatch": "^9.0.3",
        "muggle-string": "^0.3.1",
        "path-browserify": "^1.0.1",
        "vue-template-compiler": "^2.7.14"
      },
      "peerDependencies": {
        "typescript": "*"
      },
      "peerDependenciesMeta": {
        "typescript": {
          "optional": true
        }
      }
    },
    "node_modules/@vue/reactivity": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/reactivity/-/reactivity-3.4.21.tgz",
      "integrity": "sha512-UhenImdc0L0/4ahGCyEzc/pZNwVgcglGy9HVzJ1Bq2Mm9qXOpP8RyNTjookw/gOCUlXSEtuZ2fUg5nrHcoqJcw==",
      "dependencies": {
        "@vue/shared": "3.4.21"
      }
    },
    "node_modules/@vue/runtime-core": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/runtime-core/-/runtime-core-3.4.21.tgz",
      "integrity": "sha512-pQthsuYzE1XcGZznTKn73G0s14eCJcjaLvp3/DKeYWoFacD9glJoqlNBxt3W2c5S40t6CCcpPf+jG01N3ULyrA==",
      "dependencies": {
        "@vue/reactivity": "3.4.21",
        "@vue/shared": "3.4.21"
      }
    },
    "node_modules/@vue/runtime-dom": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/runtime-dom/-/runtime-dom-3.4.21.tgz",
      "integrity": "sha512-gvf+C9cFpevsQxbkRBS1NpU8CqxKw0ebqMvLwcGQrNpx6gqRDodqKqA+A2VZZpQ9RpK2f9yfg8VbW/EpdFUOJw==",
      "dependencies": {
        "@vue/runtime-core": "3.4.21",
        "@vue/shared": "3.4.21",
        "csstype": "^3.1.3"
      }
    },
    "node_modules/@vue/server-renderer": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/server-renderer/-/server-renderer-3.4.21.tgz",
      "integrity": "sha512-aV1gXyKSN6Rz+6kZ6kr5+Ll14YzmIbeuWe7ryJl5muJ4uwSwY/aStXTixx76TwkZFJLm1aAlA/HSWEJ4EyiMkg==",
      "dependencies": {
        "@vue/compiler-ssr": "3.4.21",
        "@vue/shared": "3.4.21"
      },
      "peerDependencies": {
        "vue": "3.4.21"
      }
    },
    "node_modules/@vue/shared": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/@vue/shared/-/shared-3.4.21.tgz",
      "integrity": "sha512-PuJe7vDIi6VYSinuEbUIQgMIRZGgM8e4R+G+/dQTk0X1NEdvgvvgv7m+rfmDH1gZzyA1OjjoWskvHlfRNfQf3g=="
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true
    },
    "node_modules/brace-expansion": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz",
      "integrity": "sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==",
      "dev": true,
      "dependencies": {
        "balanced-match": "^1.0.0"
      }
    },
    "node_modules/computeds": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/computeds/-/computeds-0.0.1.tgz",
      "integrity": "sha512-7CEBgcMjVmitjYo5q8JTJVra6X5mQ20uTThdK+0kR7UEaDrAWEQcRiBtWJzga4eRpP6afNwwLsX2SET2JhVB1Q==",
      "dev": true
    },
    "node_modules/csstype": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz",
      "integrity": "sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw=="
    },
    "node_modules/de-indent": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/de-indent/-/de-indent-1.0.2.tgz",
      "integrity": "sha512-e/1zu3xH5MQryN2zdVaF0OrdNLUbvWxzMbi+iNA6Bky7l1RoP8a2fIbRocyHclXt/arDrrR6lL3TqFD9pMQTsg==",
      "dev": true
    },
    "node_modules/entities": {
      "version": "4.5.0",
      "resolved": "https://registry.npmjs.org/entities/-/entities-4.5.0.tgz",
      "integrity": "sha512-V0hjH4dGPh9Ao5p0MoRY6BVqtwCjhz6vI5LT8AJ55H+4g9/4vbHx1I54fS0XuclLhDHArPQCiMjDxjaL8fPxhw==",
      "engines": {
        "node": ">=0.12"
      },
      "funding": {
        "url": "https://github.com/fb55/entities?sponsor=1"
      }
    },
    "node_modules/esbuild": {
      "version": "0.19.12",
      "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.19.12.tgz",
      "integrity": "sha512-aARqgq8roFBj054KvQr5f1sFu0D65G+miZRCuJyJ0G13Zwx7vRar5Zhn2tkQNzIXcBrNVsv/8stehpj+GAjgbg==",
      "dev": true,
      "hasInstallScript": true,
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=12"
      },
      "optionalDependencies": {
        "@esbuild/aix-ppc64": "0.19.12",
        "@esbuild/android-arm": "0.19.12",
        "@esbuild/android-arm64": "0.19.12",
        "@esbuild/android-x64": "0.19.12",
        "@esbuild/darwin-arm64": "0.19.12",
        "@esbuild/darwin-x64": "0.19.12",
        "@esbuild/freebsd-arm64": "0.19.12",
        "@esbuild/freebsd-x64": "0.19.12",
        "@esbuild/linux-arm": "0.19.12",
        "@esbuild/linux-arm64": "0.19.12",
        "@esbuild/linux-ia32": "0.19.12",
        "@esbuild/linux-loong64": "0.19.12",
        "@esbuild/linux-mips64el": "0.19.12",
        "@esbuild/linux-ppc64": "0.19.12",
        "@esbuild/linux-riscv64": "0.19.12",
        "@esbuild/linux-s390x": "0.19.12",
        "@esbuild/linux-x64": "0.19.12",
        "@esbuild/netbsd-x64": "0.19.12",
        "@esbuild/openbsd-x64": "0.19.12",
        "@esbuild/sunos-x64": "0.19.12",
        "@esbuild/win32-arm64": "0.19.12",
        "@esbuild/win32-ia32": "0.19.12",
        "@esbuild/win32-x64": "0.19.12"
      }
    },
    "node_modules/estree-walker": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-2.0.2.tgz",
      "integrity": "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/he": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/he/-/he-1.2.0.tgz",
      "integrity": "sha512-F/1DnUGPopORZi0ni+CvrCgHQ5FyEAHRLSApuYWMmrbSwoN2Mn/7k+Gl38gJnR7yyDZk6WLXwiGod1JOWNDKGw==",
      "dev": true,
      "bin": {
        "he": "bin/he"
      }
    },
    "node_modules/highlight.js": {
      "version": "11.9.0",
      "resolved": "https://registry.npmjs.org/highlight.js/-/highlight.js-11.9.0.tgz",
      "integrity": "sha512-fJ7cW7fQGCYAkgv4CPfwFHrfd/cLS4Hau96JuJ+ZTOWhjnhoeN1ub1tFmALm/+lW5z4WCAuAV9bm05AP0mS6Gw==",
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/lru-cache": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz",
      "integrity": "sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==",
      "dev": true,
      "dependencies": {
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/magic-string": {
      "version": "0.30.8",
      "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.8.tgz",
      "integrity": "sha512-ISQTe55T2ao7XtlAStud6qwYPZjE4GK1S/BeVPus4jrq6JuOnQ00YKQC581RWhR122W7msZV263KzVeLoqidyQ==",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.4.15"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/minimatch": {
      "version": "9.0.3",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-9.0.3.tgz",
      "integrity": "sha512-RHiac9mvaRw0x3AYRgDC1CxAP7HTcNrrECeA8YYJeWnpo+2Q5CegtZjaotWTWxDG3UeGA1coE05iH1mPjT/2mg==",
      "dev": true,
      "dependencies": {
        "brace-expansion": "^2.0.1"
      },
      "engines": {
        "node": ">=16 || 14 >=14.17"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/muggle-string": {
      "version": "0.3.1",
      "resolved": "https://registry.npmjs.org/muggle-string/-/muggle-string-0.3.1.tgz",
      "integrity": "sha512-ckmWDJjphvd/FvZawgygcUeQCxzvohjFO5RxTjj4eq8kw359gFF3E1brjfI+viLMxss5JrHTDRHZvu2/tuy0Qg==",
      "dev": true
    },
    "node_modules/nanoid": {
      "version": "3.3.7",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.7.tgz",
      "integrity": "sha512-eSRppjcPIatRIMC1U6UngP8XFcz8MQWGQdt1MTBQ7NaAmvXDfvNxbvWV3x2y6CdEUciCSsDHDQZbhYaB8QEo2g==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/pako": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/pako/-/pako-2.1.0.tgz",
      "integrity": "sha512-w+eufiZ1WuJYgPXbV/PO3NCMEc3xqylkKHzp8bxp1uW4qaSNQUkwmLLEc3kKsfz8lpV1F8Ht3U1Cm+9Srog2ug=="
    },
    "node_modules/path-browserify": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-browserify/-/path-browserify-1.0.1.tgz",
      "integrity": "sha512-b7uo2UCUOYZcnF/3ID0lulOJi/bafxa1xPe7ZPsammBSpjSWQkjNxlt635YGS2MiR9GjvuXCtz2emr3jbsz98g==",
      "dev": true
    },
    "node_modules/picocolors": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz",
      "integrity": "sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ=="
    },
    "node_modules/postcss": {
      "version": "8.4.35",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.4.35.tgz",
      "integrity": "sha512-u5U8qYpBCpN13BsiEB0CbR1Hhh4Gc0zLFuedrHJKMctHCHAGrMdG0PRM/KErzAL3CU6/eckEtmHNB3x6e3c0vA==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "dependencies": {
        "nanoid": "^3.3.7",
        "picocolors": "^1.0.0",
        "source-map-js": "^1.0.2"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/primeflex": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/primeflex/-/primeflex-3.3.1.tgz",
      "integrity": "sha512-zaOq3YvcOYytbAmKv3zYc+0VNS9Wg5d37dfxZnveKBFPr7vEIwfV5ydrpiouTft8MVW6qNjfkaQphHSnvgQbpQ=="
    },
    "node_modules/primeicons": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/primeicons/-/primeicons-6.0.1.tgz",
      "integrity": "sha512-KDeO94CbWI4pKsPnYpA1FPjo79EsY9I+M8ywoPBSf9XMXoe/0crjbUK7jcQEDHuc0ZMRIZsxH3TYLv4TUtHmAA=="
    },
    "node_modules/primevue": {
      "version": "3.49.1",
      "resolved": "https://registry.npmjs.org/primevue/-/primevue-3.49.1.tgz",
      "integrity": "sha512-OmUTqbKbPB63Zqf7uA49cipDi+Qh+/13AYJPwgvsVsI4QmAKIkeibBwkOgj1CNIFlopfF79YmyBshFUAPqlw9A==",
      "peerDependencies": {
        "vue": "^3.0.0"
      }
    },
    "node_modules/rollup": {
      "version": "4.12.1",
      "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.12.1.tgz",
      "integrity": "sha512-ggqQKvx/PsB0FaWXhIvVkSWh7a/PCLQAsMjBc+nA2M8Rv2/HG0X6zvixAB7KyZBRtifBUhy5k8voQX/mRnABPg==",
      "dev": true,
      "dependencies": {
        "@types/estree": "1.0.5"
      },
      "bin": {
        "rollup": "dist/bin/rollup"
      },
      "engines": {
        "node": ">=18.0.0",
        "npm": ">=8.0.0"
      },
      "optionalDependencies": {
        "@rollup/rollup-android-arm-eabi": "4.12.1",
        "@rollup/rollup-android-arm64": "4.12.1",
        "@rollup/rollup-darwin-arm64": "4.12.1",
        "@rollup/rollup-darwin-x64": "4.12.1",
        "@rollup/rollup-linux-arm-gnueabihf": "4.12.1",
        "@rollup/rollup-linux-arm64-gnu": "4.12.1",
        "@rollup/rollup-linux-arm64-musl": "4.12.1",
        "@rollup/rollup-linux-riscv64-gnu": "4.12.1",
        "@rollup/rollup-linux-x64-gnu": "4.12.1",
        "@rollup/rollup-linux-x64-musl": "4.12.1",
        "@rollup/rollup-win32-arm64-msvc": "4.12.1",
        "@rollup/rollup-win32-ia32-msvc": "4.12.1",
        "@rollup/rollup-win32-x64-msvc": "4.12.1",
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/semver": {
      "version": "7.6.0",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.6.0.tgz",
      "integrity": "sha512-EnwXhrlwXMk9gKu5/flx5sv/an57AkRplG3hTK68W7FRDN+k+OWBj65M7719OkA82XLBxrcX0KSHj+X5COhOVg==",
      "dev": true,
      "dependencies": {
        "lru-cache": "^6.0.0"
      },
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz",
      "integrity": "sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/typescript": {
      "version": "5.4.2",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.4.2.tgz",
      "integrity": "sha512-+2/g0Fds1ERlP6JsakQQDXjZdZMM+rqpamFZJEKh4kwTIn3iDkgKtby0CeNd5ATNZ4Ry1ax15TMx0W2V+miizQ==",
      "devOptional": true,
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/vite": {
      "version": "5.1.5",
      "resolved": "https://registry.npmjs.org/vite/-/vite-5.1.5.tgz",
      "integrity": "sha512-BdN1xh0Of/oQafhU+FvopafUp6WaYenLU/NFoL5WyJL++GxkNfieKzBhM24H3HVsPQrlAqB7iJYTHabzaRed5Q==",
      "dev": true,
      "dependencies": {
        "esbuild": "^0.19.3",
        "postcss": "^8.4.35",
        "rollup": "^4.2.0"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^18.0.0 || >=20.0.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^18.0.0 || >=20.0.0",
        "less": "*",
        "lightningcss": "^1.21.0",
        "sass": "*",
        "stylus": "*",
        "sugarss": "*",
        "terser": "^5.4.0"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "lightningcss": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        }
      }
    },
    "node_modules/vue": {
      "version": "3.4.21",
      "resolved": "https://registry.npmjs.org/vue/-/vue-3.4.21.tgz",
      "integrity": "sha512-5hjyV/jLEIKD/jYl4cavMcnzKwjMKohureP8ejn3hhEjwhWIhWeuzL2kJAjzl/WyVsgPY56Sy4Z40C3lVshxXA==",
      "dependencies": {
        "@vue/compiler-dom": "3.4.21",
        "@vue/compiler-sfc": "3.4.21",
        "@vue/runtime-dom": "3.4.21",
        "@vue/server-renderer": "3.4.21",
        "@vue/shared": "3.4.21"
      },
      "peerDependencies": {
        "typescript": "*"
      },
      "peerDependenciesMeta": {
        "typescript": {
          "optional": true
        }
      }
    },
    "node_modules/vue-template-compiler": {
      "version": "2.7.16",
      "resolved": "https://registry.npmjs.org/vue-template-compiler/-/vue-template-compiler-2.7.16.tgz",
      "integrity": "sha512-AYbUWAJHLGGQM7+cNTELw+KsOG9nl2CnSv467WobS5Cv9uk3wFcnr1Etsz2sEIHEZvw1U+o9mRlEO6QbZvUPGQ==",
      "dev": true,
      "dependencies": {
        "de-indent": "^1.0.2",
        "he": "^1.2.0"
      }
    },
    "node_modules/vue-tsc": {
      "version": "1.8.27",
      "resolved": "https://registry.npmjs.org/vue-tsc/-/vue-tsc-1.8.27.tgz",
      "integrity": "sha512-WesKCAZCRAbmmhuGl3+VrdWItEvfoFIPXOvUJkjULi+x+6G/Dy69yO3TBRJDr9eUlmsNAwVmxsNZxvHKzbkKdg==",
      "dev": true,
      "dependencies": {
        "@volar/typescript": "~1.11.1",
        "@vue/language-core": "1.8.27",
        "semver": "^7.5.4"
      },
      "bin": {
        "vue-tsc": "bin/vue-tsc.js"
      },
      "peerDependencies": {
        "typescript": "*"
      }
    },
    "node_modules/yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==",
      "dev": true
    }
  }
}
================================================

File: package.json
================================================
{
  "name": "mikrotik-rif-viewer",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@highlightjs/vue-plugin": "^2.1.0",
    "highlight.js": "^11.9.0",
    "pako": "^2.1.0",
    "primeflex": "^3.3.1",
    "primeicons": "^6.0.1",
    "primevue": "^3.49.1",
    "vue": "^3.4.19"
  },
  "devDependencies": {
    "@types/pako": "^2.0.3",
    "@vitejs/plugin-vue": "^5.0.4",
    "typescript": "^5.2.2",
    "vite": "^5.1.4",
    "vue-tsc": "^1.8.27"
  }
}
================================================

File: README.md
================================================
# Mikrotik RIF Viewer
This tool allows you to view the complete contents of `supout.rif` files with basic (and somewhat random) syntax highlighting.
It basically serves the same purpose as the viewer provided by Mikrotik themselves, except that it doesn't hide anything, looks better and doesn't require sending the files to any backend (all processing is done locally in the browser).
![Screenshot of the UI](./screenshot.png)
## Usage
1. [Open the tool](https://mikrotik-rif-viewer-derenderkeks-87883f8fa0a3e6e6625c350569ddd8.gitlab.io)
2. Drag and drop the `supout.rif` file into the upload box (or click the upload button and select it)
3. Click the section of interest
4. ???
5. Profit!
### Docker Container
* NOTE: While the default `vite` config of this tool will only be reachable from localhost, this container will be reachable from other hosts as well
1. Build the container
```
docker compose build		# or docker-compose build    		depending on your setup
```
2. Run the container
```
docker compose up -d		# or docker-compose up -d     		depending on your setup
```
3. The service will be running on `TCP 4242`, you can reach it by opening `http://YOUR_SERVERS_IP_ADDRESS:4242/` in your browser
================================================

File: tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": [
      "ESNext",
      "ES2020",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": [
    "src/**/*.ts",
    "src/**/*.tsx",
    "src/**/*.vue"
  ],
  "references": [
    {
      "path": "./tsconfig.node.json"
    }
  ]
}
================================================

File: tsconfig.node.json
================================================
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "strict": true
  },
  "include": ["vite.config.ts"]
}
================================================

File: vite.config.ts
================================================
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    target: ['es2022']
  },
})