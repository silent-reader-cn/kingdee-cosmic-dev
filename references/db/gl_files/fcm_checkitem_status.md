# 检查项状态控制辅助表-fcm_checkitem_status

## 检查项状态控制辅助表-主表 t_fcm_checkitemstatus

- **表名称：** 检查项状态控制辅助表-主表
- **表名：** t_fcm_checkitemstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubbizappid | 账簿 | varchar | 30 |  | √ | ' ' | 账簿,枚举: |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 使用组织 |
| 5 | fcheckitemid | 检查项ID | int8 | 64 |  | √ | 0 | 检查项ID |
| 6 | fiseffective | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |
| 7 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_checkitemstatus |  | fid |
| 2 | idx_fcmstatus_org |  | fuseorgid |
| 3 | idx_fcmstatus_cii |  | fcheckitemid |
