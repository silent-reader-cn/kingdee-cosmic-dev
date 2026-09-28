# 外部系统组织-bdm_third_org

## 外部系统组织-主表 t_bdm_third_org

- **表名称：** 外部系统组织-主表
- **表名：** t_bdm_third_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_name | 租户名称 | varchar | 150 |  | √ | ' ' | 租户名称 |
| 3 | fthird_org_no | 第三方组织编码 | varchar | 150 |  | √ | ' ' | 第三方组织编码 |
| 4 | ftenant_no | 租户编码 | varchar | 50 |  | √ | ' ' | 租户编码 |
| 5 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | forg_no | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_third_org |  | fthird_org_no |
| 2 | pk_bdm_third_org |  | fid |
