# 个人设置后台-em_m_usersetting

## 个人设置后台-主表 t_er_usersetting

- **表名称：** 个人设置后台-主表
- **表名：** t_er_usersetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fotherinfo | 扩展信息 | text | 0 |  |  | null | 扩展信息 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 5 | fotherinfo_tag | 扩展信息_详情 | varchar | 60 |  | √ | ' ' | 扩展信息_详情 |
| 6 | fcurrencyid | 报告币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | funit | 单位 | varchar | 5 |  | √ | '0' | 单位,枚举: 0 :元 1 :千 2 :万 3 :亿 4 :十亿 99 :自适应 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_m_uset_user |  | fuserid |
| 2 | pk_t_em_usersetting |  | fid |
