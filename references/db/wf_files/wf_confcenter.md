# 工作流配置中心-wf_confcenter

## 工作流配置中心-主表 t_wf_confcenter

- **表名称：** 工作流配置中心-主表
- **表名：** t_wf_confcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 2000 |  | √ | ' ' | 值 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: global :全局 message :消息 dynamic :动态 |
| 4 | fkey | 键 | varchar | 255 |  | √ | ' ' | 键 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_confcenter_pkey |  | fid |
| 2 | idx_wf_confcenter_fkey |  | fkey |
