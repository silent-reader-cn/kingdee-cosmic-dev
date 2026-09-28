# 城市以及热门航线汇总-er_city_routes_summary

## 城市以及热门航线汇总-主表 t_er_city_routes_summary

- **表名称：** 城市以及热门航线汇总-主表
- **表名：** t_er_city_routes_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织ID | varchar | 50 |  | √ | ' ' | 组织ID |
| 3 | fcityjson_tag | 属性集合_详情 | text | 0 |  |  | ' ' | 属性集合_详情 |
| 4 | fsummaryend | 汇总结束日期 | timestamp | 0 |  |  | null | 汇总结束日期 |
| 5 | fcityjson | 属性集合 | varchar | 255 |  | √ | ' ' | 属性集合 |
| 6 | fsummarystart | 汇总开始日期 | timestamp | 0 |  |  | null | 汇总开始日期 |
| 7 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: Route :航线 City :城市 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_city_routes_summary |  | fsummarystart,fsummaryend,forgid |
| 2 | pk_t_er_city_routes_summary |  | fid |
