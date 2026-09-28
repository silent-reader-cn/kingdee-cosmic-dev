# 全员应用黑名单-alluserappblacklist

## 全员应用黑名单-主表 t_perm_appblacklist

- **表名称：** 全员应用黑名单-主表
- **表名：** t_perm_appblacklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisincludesuborg | 所有下级受控 | bpchar | 1 |  | √ | '0' | 所有下级受控 |
| 3 | forgid | 受控组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fappid | 应用 | varchar | 18 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_appblacklist_pkey |  | fid |
| 2 | ix_perm_appblacklist_orgid |  | forgid |
