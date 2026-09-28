# 信息确认-tcvvt_message

## 单据体-子表 t_tcvvt_xxqr_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvvt_xxqr_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fselectid | 选择的id | int8 | 64 |  | √ | 0 | 选择的id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_xxqr_entry |  | fentryid |
| 2 | idx_tcvvt_xxqr_entry_fk |  | fid |

---

## 信息确认-主表 t_tcvvt_message

- **表名称：** 信息确认-主表
- **表名：** t_tcvvt_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 |
| 4 | fregisteraddress | 注册登记区域： | varchar | 50 |  | √ | ' ' | 注册登记区域： |
| 5 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 6 | fstartdate | 开始时间： | timestamp | 0 |  |  | null | 开始时间： |
| 7 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fnewrule | 执行新准则： | varchar | 50 |  | √ | ' ' | 执行新准则：,枚举: yes :已执行 no :未执行 |
| 9 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: aysb :月度 ajsb :季度 ansb :年度 |
| 10 | fdeclaretype | 申报企业类型： | varchar | 50 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 11 | fdeclaretype1criterion | 会计准则或会计制度： | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_message |  | fenddate,forgid,fstartdate,freporttype |
| 2 | pk_tcvvt_message |  | fid |
