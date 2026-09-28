# 受控章信息-plmdc_controlledseal

## 受控章信息-主表 t_plmdc_controlledseal

- **表名称：** 受控章信息-主表
- **表名：** t_plmdc_controlledseal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbottommargin | 下边距 | int4 | 32 |  | √ | 0 | 下边距 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fsize | 大小比例 | int4 | 32 |  | √ | 0 | 大小比例 |
| 5 | fadjustdimension | 调整维度 | varchar | 50 |  | √ | ' ' | 调整维度,枚举: proportion :比例（%） size :尺寸（PX） |
| 6 | fpicturefield | 签章图片 | varchar | 255 |  | √ | ' ' | 签章图片 |
| 7 | fposition | 签章位置 | varchar | 50 |  | √ | ' ' | 签章位置,枚举: LU :左上 LD :左下 RU :右上 RD :右下 |
| 8 | fleftmargin | 左边距 | int4 | 32 |  | √ | 0 | 左边距 |
| 9 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_controlledseal |  | fid |
| 2 | idx_plmdc_controlledseal_name |  | fname |
