# 经营报告配置-mai_bizreportcfg

## 经营报告配置-主表 t_mai_bizreportcfg

- **表名称：** 经营报告配置-主表
- **表名：** t_mai_bizreportcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 报告名称 | varchar | 20 |  | √ | ' ' | 报告名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdefault | 默认展示 | bpchar | 1 |  | √ | '0' | 默认展示 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :启用 |
| 11 | fbillno | 报告编码 | varchar | 30 |  | √ | '0' | 报告编码 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftemplate | 模板 | bpchar | 1 |  | √ | '0' | 模板,枚举: 0 :销售日报 1 :经营月报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mai_bizreportcfg |  | fid |
| 2 | idx_mai_bizreportcfg_fbillno |  | fbillno |
