# 其他数据中心用户-ippm_otheraccountuser

## 其他数据中心用户-主表 t_ippm_otheraccountuser

- **表名称：** 其他数据中心用户-主表
- **表名：** t_ippm_otheraccountuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | favatar | 人员头像 | varchar | 255 |  | √ | ' ' | 人员头像 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_otheraccountuser |  | fname |
| 2 | pk_t_ippm_otheraccountuser |  | fid |
