# 核算过滤配置-cal_filter_config

## 核算过滤配置-主表 t_cal_filter_config

- **表名称：** 核算过滤配置-主表
- **表名：** t_cal_filter_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fuse | 用途 | varchar | 30 |  | √ | ' ' | 用途,枚举: costrecformula :成本记录取数公式 costadjformula :成本调整单取数公式 |
| 4 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 5 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 7 | fentityid | 业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_filter_num |  | fnumber |
| 2 | idx_cal_filter_entuse |  | fentityid,fuse |
| 3 | pk_t_cal_filter_config |  | fid |
