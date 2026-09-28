# 二次认证受控组织-bos_confirm_orgentity

## 二次认证受控组织-主表 t_bd_signconfirmorg

- **表名称：** 二次认证受控组织-主表
- **表名：** t_bd_signconfirmorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | ' ' | 包含下级 |
| 3 | forgid | 受控组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fschemeid | 二次认证方案id | int8 | 64 |  | √ | 0 | 二次认证方案id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_operate_s_id |  | fschemeid |
| 2 | pk_bd_signconfirmorg |  | fid |
