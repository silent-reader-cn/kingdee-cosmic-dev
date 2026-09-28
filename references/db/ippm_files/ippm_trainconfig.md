# 培训配置-ippm_trainconfig

## 培训配置-主表 t_ippm_trainconfig

- **表名称：** 培训配置-主表
- **表名：** t_ippm_trainconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsecret | 客户密钥 | varchar | 255 |  | √ | ' ' | 客户密钥 |
| 3 | fenvironmentid | 环境ID | varchar | 255 |  | √ | ' ' | 环境ID |
| 4 | fenvtype | 环境类型 | varchar | 50 |  | √ | ' ' | 环境类型,枚举: test :测试环境 prod :生产环境 prod_release :生产网关-预发布环境 test_release :测试网关-预发布环境 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_trainconfig |  | fid |
| 2 | idx_ippm_trainconfig |  | fenvtype |
