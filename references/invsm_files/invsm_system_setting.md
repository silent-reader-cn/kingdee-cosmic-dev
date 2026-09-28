# 系统设置-invsm_system_setting

## 系统设置-主表 t_invsm_system_setting

- **表名称：** 系统设置-主表
- **表名：** t_invsm_system_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 3 | fqrcodeday | 二维码有效期（天） | int8 | 64 |  | √ | 0 | 二维码有效期（天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invsm_system_setting |  | fid |
| 2 | idx_invsm_system_setting |  | ftaxno |
