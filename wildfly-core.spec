%bcond_with legacy_test
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:                wildfly-core
Version:             2.2.0
Release:             4
Summary:             The core run-time of WildFly
License:             ASL 2.0 and BSD and LGPLv2+
URL:                 http://wildfly.org/
Source0:             https://github.com/wildfly/wildfly-core/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
BuildRequires:       maven-local mvn(io.undertow:undertow-core) >= 1.4.0 mvn(junit:junit)
BuildRequires:       mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.maven:maven-aether-provider)
BuildRequires:       mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:       mvn(org.codehaus.plexus:plexus-utils) mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:       mvn(org.codehaus.woodstox:woodstox-core-asl) mvn(org.eclipse.aether:aether-api)
BuildRequires:       mvn(org.eclipse.aether:aether-spi) mvn(org.eclipse.aether:aether-util)
BuildRequires:       mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:       mvn(org.eclipse.aether:aether-transport-file)
BuildRequires:       mvn(org.eclipse.aether:aether-transport-http) mvn(org.fusesource.jansi:jansi)
BuildRequires:       mvn(org.jboss:jandex) mvn(org.jboss:jboss-dmr) >= 1.3.0
BuildRequires:       mvn(org.jboss:jboss-parent:pom:) mvn(org.jboss:jboss-vfs)
BuildRequires:       mvn(org.jboss:staxmapper) >= 1.2.0 mvn(org.jboss.aesh:aesh) >= 0.66.8
BuildRequires:       mvn(org.jboss.byteman:byteman)
BuildRequires:       mvn(org.jboss.classfilewriter:jboss-classfilewriter) >= 1.1.2
BuildRequires:       mvn(org.jboss.invocation:jboss-invocation)
BuildRequires:       mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires:       mvn(org.jboss.logging:jul-to-slf4j-stub)
BuildRequires:       mvn(org.jboss.logmanager:jboss-logmanager) >= 2.0.4
BuildRequires:       mvn(org.jboss.logmanager:log4j-jboss-logmanager) >= 1.1.2-2
BuildRequires:       mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:       mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires:       mvn(org.jboss.modules:jboss-modules) >= 1.5.2 mvn(org.jboss.msc:jboss-msc)
BuildRequires:       mvn(org.jboss.remoting:jboss-remoting) mvn(org.jboss.remotingjmx:remoting-jmx)
BuildRequires:       mvn(org.jboss.sasl:jboss-sasl) >= 1.0.5
BuildRequires:       mvn(org.jboss.slf4j:slf4j-jboss-logmanager)
BuildRequires:       mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:       mvn(org.jboss.stdio:jboss-stdio) mvn(org.jboss.threads:jboss-threads)
BuildRequires:       mvn(org.jboss.xnio:xnio-api) mvn(org.jboss.xnio:xnio-nio)
BuildRequires:       mvn(org.picketbox:picketbox) >= 4.9.5 mvn(org.slf4j:slf4j-api)
BuildRequires:       mvn(org.wildfly.build:wildfly-feature-pack-build-maven-plugin)
BuildRequires:       mvn(org.wildfly.build:wildfly-server-provisioning-maven-plugin)
BuildRequires:       mvn(org.wildfly.common:wildfly-common)
BuildRequires:       mvn(org.wildfly.security:wildfly-elytron) mvn(xerces:xercesImpl)
BuildRequires:       mvn(xml-resolver:xml-resolver) xmvn
%if %{with legacy_test}
BuildRequires:       mvn(com.google.guava:guava) mvn(commons-io:commons-io)
BuildRequires:       mvn(commons-lang:commons-lang) mvn(javax.inject:javax.inject)
BuildRequires:       mvn(log4j:log4j:12) mvn(org.apache.directory.api:api-ldap-codec-standalone)
BuildRequires:       mvn(org.apache.directory.jdbm:apacheds-jdbm1:bundle:)
BuildRequires:       mvn(org.apache.directory.server:apacheds-core-annotations)
BuildRequires:       mvn(org.apache.directory.server:apacheds-interceptor-kerberos)
BuildRequires:       mvn(org.apache.directory.server:apacheds-parent:pom:)
BuildRequires:       mvn(org.apache.directory.server:apacheds-server-annotations)
BuildRequires:       mvn(org.apache.httpcomponents:httpclient)
BuildRequires:       mvn(org.apache.httpcomponents:httpcore) mvn(org.apache.httpcomponents:httpmime)
BuildRequires:       mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:       mvn(org.codehaus.mojo:keytool-api-1.7)
BuildRequires:       mvn(org.codehaus.mojo:keytool-maven-plugin)
BuildRequires:       mvn(org.codehaus.mojo:xml-maven-plugin) mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires:       mvn(org.jboss.byteman:byteman-install) mvn(org.jboss.byteman:byteman-submit)
BuildRequires:       mvn(org.jboss.metadata:jboss-metadata-common) >= 10.0.0
BuildRequires:       mvn(org.jboss.shrinkwrap:shrinkwrap-api)
BuildRequires:       mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base) mvn(org.mockito:mockito-all)
BuildRequires:       mvn(org.slf4j:jcl-over-slf4j) mvn(org.syslog4j:syslog4j)
BuildRequires:       mvn(org.wildfly.legacy.test:wildfly-legacy-spi)
%endif
Provides:            bundled(apache-common-codec) = 1.7
BuildArch:           noarch
%description
This project provides the core run-time that is used by the
Wildfly application server. This includes:
* Modular class loading
* Unified management, including domain mode
* Basic deployment architecture
* CLI for management

%package javadoc
Summary:             Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%package feature-pack
Summary:             WildFly: Core Feature Pack
%description feature-pack
WildFly:             Core Feature Pack.

%prep
%setup -q -n %{name}-%{namedversion}
%if %{without legacy_test}
%pom_disable_module subsystem-test
%pom_disable_module testsuite
%pom_disable_module tests remoting
%pom_disable_module tests io
%pom_disable_module core-model-test
%pom_remove_dep -r org.wildfly.core:wildfly-core-model-test-framework
%pom_remove_dep -r org.apache.directory.server:apacheds-parent
%else
%pom_xpath_set "pom:properties/pom:version.log4j" 1.2.17
%endif
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r org.zanata:zanata-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_dep -r :wildfly-checkstyle-config
%pom_remove_dep sun.jdk:jconsole cli
%pom_add_dep sun.jdk:jconsole cli
cp -p core-feature-pack/src/main/resources/content/LICENSE.txt .
%mvn_package ":wildfly-core-feature-pack" core-feature-pack
%mvn_package ":wildfly-core-dist:::" __noinstall
%mvn_package ":wildfly-core-build:zip::" __noinstall
%mvn_package ":wildfly-core-build:::" __noinstall

%build
%mvn_build -f -- -X
rm target/site/apidocs/javadoc.sh

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files feature-pack -f .mfiles-core-feature-pack
%license LICENSE.txt

%changelog
* Wed Dec 29 2021 wangkai <wangkai385@huawei.com> - 2.2.0-4
- This package depends on log4j.After the log4j vulnerability CVE-2021-44832 is fixed,the version needs to be rebuild.

* Fri Dec 24 2021 wangkai <wangkai385@huawei.com> - 2.2.0-3
- This package depends on log4j.After the log4j vulnerability CVE-2021-45105 is fixed,the version needs to be rebuild.

* Thu Dec 16 2021 wangkai <wangkai385@huawei.com> - 2.2.0-2
- This package depends on log4j.After the log4j vulnerability CVE-2021-44228 is fixed,the version needs to be rebuild.

* Wed Aug 19 2020 maminjie <maminjie1@huawei.com> - 2.2.0-1
- package init
