# 高新未分摊（临时）-rdem_fzzmx_gx_wft_tp

## 高新未分摊（临时）-主表 t_rdem_fzzmx_gx_wft_tp

- **表名称：** 高新未分摊（临时）-主表
- **表名：** t_rdem_fzzmx_gx_wft_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 记账凭证类型 | varchar | 50 |  | √ | ' ' | 记账凭证类型 |
| 3 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 2 | √ | 0 | 借方本币金额 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fgjrepeatstatus | 归集重复情况 | varchar | 50 |  | √ | ' ' | 归集重复情况,枚举: 0 :否 1 :是 |
| 6 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsourceid | 数据来源实体id | int8 | 64 |  | √ | 0 | 数据来源实体id |
| 9 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 10 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 11 | fbkjjkc | 不可研发加计 | bpchar | 1 |  | √ | '0' | 不可研发加计 |
| 12 | fallocatestatus | 是否分摊 | varchar | 50 |  | √ | ' ' | 是否分摊,枚举: 0 :无需分摊 1 :是 2 :否 |
| 13 | fbaseproject | 系统项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 14 | fftrule | 分摊配置单据体的id | varchar | 2000 |  | √ | ' ' | 分摊配置单据体的id |
| 15 | fpersonno | 人员工号 | varchar | 50 |  | √ | ' ' | 人员工号 |
| 16 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 17 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fmonth | 月份 | int8 | 64 |  | √ | 0 | 月份 |
| 19 | fpersonname | 人员名称 | varchar | 50 |  | √ | ' ' | 人员名称 |
| 20 | fgjysz | 归集要素值 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fgjyslx | 归集要素类型 | varchar | 50 |  | √ | ' ' | 归集要素类型,枚举: bos_costcenter :成本中心 bd_project :项目 |
| 22 | fvoucherremark | 记账凭证摘要 | varchar | 2000 |  | √ | ' ' | 记账凭证摘要 |
| 23 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 24 | fbalancelocalcurrency | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 25 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 26 | frepeatstatus | 归集与分摊重复情况 | varchar | 50 |  | √ | ' ' | 归集与分摊重复情况,枚举: 0 :不重复 1 :归集重复 2 :分摊重复 3 :归集和分摊都重复 |
| 27 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 2 | √ | 0 | 贷方本币金额 |
| 28 | fwithinallocate | 是否处于分摊范围内 | varchar | 50 |  | √ | ' ' | 是否处于分摊范围内,枚举: 1 :是 0 :否 |
| 29 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 30 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 31 | fbalanceid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 32 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [高新费用类别 rdem_high_tech_costtype](../rdem_files/rdem_high_tech_costtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzzmx_gx_wft_tp |  | fid |
