# 合规性校验修改历史-rim_verify_modify_his

## 合规性校验修改历史-主表 t_rim_verify_modify_his

- **表名称：** 合规性校验修改历史-主表
- **表名：** t_rim_verify_modify_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodify_name | 修改内容NAME | varchar | 100 |  | √ | ' ' | 修改内容NAME |
| 3 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 4 | fafter_value | 修改后的值 | varchar | 300 |  | √ | ' ' | 修改后的值 |
| 5 | fbefore_value | 修改前的值 | varchar | 300 |  | √ | ' ' | 修改前的值 |
| 6 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fmodify_key | 修改内容KEY | varchar | 50 |  | √ | ' ' | 修改内容KEY |
| 8 | fmodifier | 修改人 | varchar | 36 |  | √ | ' ' | 修改人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_verify_modify_his |  | fid |
| 2 | idx_rim_serial_no |  | fserial_no |
