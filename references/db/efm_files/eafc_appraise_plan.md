# 保管期限鉴定-eafc_appraise_plan

## 保管期限鉴定-主表 tk_eafc_appraise_plan

- **表名称：** 保管期限鉴定-主表
- **表名：** tk_eafc_appraise_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_expire_time |  | timestamp | 0 |  |  | null |  |
| 3 | fk_eafc_plan | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: 1 :档案销毁 2 :延迟保管年限 3 :调整保管期限为 4 :调整档案到期时间为 |
| 4 | fk_eafc_year | 年 | int8 | 64 |  |  | null | 年 |
| 5 | fk_eafc_storage |  | varchar | 50 |  | √ | ' ' | ,枚举: 1 :10年 2 :30年 3 :永久 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_appraise_plan |  | fid |
