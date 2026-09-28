# 出纳对账方案-cas_checkscheme

## 出纳对账方案-主表 t_cas_checkscheme

- **表名称：** 出纳对账方案-主表
- **表名：** t_cas_checkscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisbizdate | 日期相同 | bpchar | 1 |  | √ | '0' | 日期相同 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdatediffcount | 日期相差天数 | int8 | 64 |  | √ | 0 | 日期相差天数 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fisoppunit | 对方单位相同 | bpchar | 1 |  | √ | '0' | 对方单位相同 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fisdescription | 摘要相同 | bpchar | 1 |  | √ | '0' | 摘要相同 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fissettlementtype | 结算方式相同 | bpchar | 1 |  | √ | '0' | 结算方式相同 |
| 14 | fischeckflag | 对账码相同 | bpchar | 1 |  | √ | '0' | 对账码相同 |
| 15 | fisdatediff | 日期相差 | bpchar | 1 |  | √ | '0' | 日期相差 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fissettlenum4schedule | 结算号相同 | bpchar | 1 |  | √ | '0' | 结算号相同 |
| 19 | fissettlenum4auto | 结算号相同 | bpchar | 1 |  | √ | '0' | 结算号相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cas_scehme_org |  | forgid |
| 2 | t_cas_checkscheme_pkey |  | fid |
