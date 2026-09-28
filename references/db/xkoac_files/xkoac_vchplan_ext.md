# 经营会计扩展方案-xkoac_vchplan_ext

## 经营会计扩展方案-主表 t_xkoac_vchplan_ext

- **表名称：** 经营会计扩展方案-主表
- **表名：** t_xkoac_vchplan_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffieldtype | 目标单据扩展字段所在实体 | bpchar | 1 |  | √ | '1' | 目标单据扩展字段所在实体,枚举: 1 :单据头 2 :单据体 |
| 3 | fvchextfield | 目标单据扩展字段标识 | varchar | 100 |  | √ | ' ' | 目标单据扩展字段标识 |
| 4 | fbilltype | 目标单据 | bpchar | 1 |  | √ | '1' | 目标单据,枚举: 1 :经营流水账 2 :经营费用归集单 3 :经营费用分摊结果单 |
| 5 | fplanextfield | 方案扩展字段标识 | varchar | 100 |  | √ | ' ' | 方案扩展字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_vchplan_ext_fplanex |  | fplanextfield |
| 2 | pk_xkoac_vchplan_ext |  | fid |
