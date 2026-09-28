# 渠道分类标准应用-ocdbd_channel_std_apply

## 渠道分类标准应用-主表 t_ocdbd_chl_apply

- **表名称：** 渠道分类标准应用-主表
- **表名：** t_ocdbd_chl_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 应用场景名称 | varchar | 80 |  | √ | ' ' | 应用场景名称,枚举: 0 :可销商品设置 1 :订货批量设置 2 :价格政策设置 3 :促销政策设置 4 :返利政策设置 5 :零售经营目录 |
| 3 | fclassstandardid | 渠道分类标准 | int8 | 64 |  | √ | 0 | 渠道分类标准 ocdbd_channel_standard |
| 4 | fnumber | 应用场景编码 | varchar | 80 |  | √ | ' ' | 应用场景编码 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chl_apply |  | fid |
| 2 | idx_ocdbd_chlapply_num |  | fnumber |
