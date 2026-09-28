# 影像参数配置-bos_imageparamsconfig

## 影像参数配置-主表 t_bos_imageparamsconfig

- **表名称：** 影像参数配置-主表
- **表名：** t_bos_imageparamsconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 参数值 | varchar | 200 |  | √ | ' ' | 参数值 |
| 3 | fkey | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 4 | fdesc | 参数描述 | varchar | 200 |  | √ | ' ' | 参数描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bos_imageparamsconfig |  | fid |
| 2 | idx_bos_paramscofig_key |  | fkey |
