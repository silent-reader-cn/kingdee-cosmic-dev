# 辅助账明细（临时已分摊）-rdem_fzzmx_yft_tp

## 辅助账明细（临时已分摊）-主表 t_rdem_fzzmx_yft_tp

- **表名称：** 辅助账明细（临时已分摊）-主表
- **表名：** t_rdem_fzzmx_yft_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 记账凭证类型 | varchar | 50 |  | √ | ' ' | 记账凭证类型 |
| 3 | fgjyslx | 归集要素类型 | varchar | 50 |  | √ | ' ' | 归集要素类型,枚举: bos_costcenter :成本中心 bd_project :项目 |
| 4 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 5 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 2 | √ | 0 | 借方本币金额 |
| 6 | fvoucherremark | 记账凭证摘要 | varchar | 2000 |  | √ | ' ' | 记账凭证摘要 |
| 7 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbalancelocalcurrency | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 9 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 10 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 12 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 13 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 |
| 14 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 15 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 2 | √ | 0 | 贷方本币金额 |
| 16 | fbaseproject | 系统项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fprecost | 上一级费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |
| 18 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 19 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 20 | fbalanceid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 21 | fisvalid | 是否有效 | bpchar | 1 |  | √ | '0' | 是否有效 |
| 22 | fgjysz | 归集要素值 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: dsyj :第三季度预缴 hsqj :年度汇算清缴 |
| 24 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzzmx_yft_tp |  | fid |
| 2 | idx_rdem_fzzmx_yft_tp_m0 |  | fisvalid |
