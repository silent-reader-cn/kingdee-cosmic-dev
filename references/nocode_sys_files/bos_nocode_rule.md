# 规则配置-bos_nocode_rule

## 规则配置-主表 t_nocode_ruleconfig

- **表名称：** 规则配置-主表
- **表名：** t_nocode_ruleconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fexpression | 条件 | text | 0 |  |  | null | 条件 |
| 4 | fdepfldkeys | 依赖字段 | varchar | 2000 |  | √ | ' ' | 依赖字段 |
| 5 | ftrueaction | 执行动作 | text | 0 |  |  | null | 执行动作 |
| 6 | fruletype | 规则类型 | bpchar | 1 |  | √ | '0' | 规则类型,枚举: 0 :界面规则 1 :业务规则 |
| 7 | faffectfldkeys | 影响字段 | varchar | 2000 |  | √ | ' ' | 影响字段 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fvaluetype | 值类型 | bpchar | 1 |  | √ | '0' | 值类型,枚举: 0 :查找值写入 1 :运算公式 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fformid | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_nocode_ruleconfig |  | fid |
| 2 | idx_nc_rule_formid |  | fformid |
