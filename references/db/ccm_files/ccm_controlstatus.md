# 维度成员值受控状态-ccm_controlstatus

## 维度成员值受控状态-主表 t_ccm_controlstatus

- **表名称：** 维度成员值受控状态-主表
- **表名：** t_ccm_controlstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | froleid | 维度成员 | int8 | 64 |  | √ | 0 | [维度成员 ccm_role](../ccm_files/ccm_role.md) |
| 3 | frolevalueid | 维度成员值id | int8 | 64 |  | √ | 0 | 维度成员值id |
| 4 | fcontrolstatus | 受控状态 | varchar | 30 |  | √ | ' ' | 受控状态,枚举: 0 :不受控 1 :受控 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_controlstatus |  | fid |
| 2 | idx_ccm_cs_frolevalueid |  | frolevalueid |
