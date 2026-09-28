# 分摊结果表（临时）-rdem_fzz_ftjg_tp

## 分摊结果表（临时）-主表 t_rdem_fzz_ftjg_tp

- **表名称：** 分摊结果表（临时）-主表
- **表名：** t_rdem_fzz_ftjg_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 记账凭证类型 | varchar | 50 |  | √ | ' ' | 记账凭证类型 |
| 3 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 2 | √ | 0 | 借方本币金额 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 8 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fpersonno | 人员工号 | varchar | 50 |  | √ | ' ' | 人员工号 |
| 11 | fgroupdime | 分组维度 | varchar | 50 |  | √ | ' ' | 分组维度,枚举: taxorg :税务组织 costcenter :成本中心 staffnumber :人员工号 |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fpersonname | 人员名称 | varchar | 50 |  | √ | ' ' | 人员名称 |
| 14 | fcostcenterid | 成本中心名称 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | fshareratio | 分摊比例 | numeric | 23 | 10 | √ | 0 | 分摊比例 |
| 16 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 17 | fvoucherremark | 记账凭证摘要 | varchar | 2000 |  | √ | ' ' | 记账凭证摘要 |
| 18 | fbalancelocalcurrency | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 19 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 |
| 20 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 21 | frepeatstatus | 凭证是否重复 | varchar | 50 |  | √ | ' ' | 凭证是否重复,枚举: 0 :不重复 1 :重复 |
| 22 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 2 | √ | 0 | 贷方本币金额 |
| 23 | fgjfyid | 费用归集 | int8 | 64 |  | √ | 0 | 辅助账明细（未分摊-临时） rdem_fzzmx_wft_tp |
| 24 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 25 | fbalanceid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 26 | fsharetypeid | 分摊类型 | int8 | 64 |  | √ | 0 | [分摊类型 rdem_share_type](../rdem_files/rdem_share_type.md) |
| 27 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzz_ftjg_tp |  | fid |
| 2 | idx_rdem_fzz_ftjg_tp_m0 |  | fcreatedate |
