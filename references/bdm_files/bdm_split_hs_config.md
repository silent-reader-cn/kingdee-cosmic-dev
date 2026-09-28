# 含税拆分-bdm_split_hs_config

## 含税拆分-主表 t_bdm_split_hs_config

- **表名称：** 含税拆分-主表
- **表名：** t_bdm_split_hs_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumberdigitrule | 数量位数规则 | varchar | 4 |  | √ | '1' | 数量位数规则,枚举: 1 :单行商品税额误差超过范围时，以系统计算为准 2 :单行商品税额误差超过范围时，强制保留数量位数，反算不含税单价 |
| 3 | forgs_tag | 分配组织_详情 | text | 0 |  |  | null | 分配组织_详情 |
| 4 | forgs | 分配组织 | varchar | 255 |  | √ | ' ' | 分配组织 |
| 5 | fnormalelectroniclimit | 电子普票含税限额 | numeric | 23 | 10 | √ | 0 | 电子普票含税限额 |
| 6 | fspecialelectroniclimit | 电子专票含税限额 | numeric | 23 | 10 | √ | 0 | 电子专票含税限额 |
| 7 | fftaxcalculatetype | 税额计算方式 | varchar | 2 |  | √ | ' ' | 税额计算方式,枚举: 0 :以实际输入税额为准，系统不调整税额误差 1 :以系统计算为准，系统将调整误差 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fspecialallelimit | 全电专票含税限额 | numeric | 23 | 10 | √ | 0 | 全电专票含税限额 |
| 10 | fspecialpaperlimit | 纸质专票含税限额 | numeric | 23 | 10 | √ | 0 | 纸质专票含税限额 |
| 11 | fnormalallelimit | 全电普票含税限额 | numeric | 23 | 10 | √ | 0 | 全电普票含税限额 |
| 12 | fnormalpaperlimit | 纸质普票含税限额 | numeric | 23 | 10 | √ | 0 | 纸质普票含税限额 |
| 13 | fsplitrule | 含税拆分规则 | varchar | 4 |  | √ | '1' | 含税拆分规则,枚举: 1 :按照数量，单价不变 2 :按照数量，接近顶额开具 3 :按照单价拆分，数量不变 |
| 14 | fnumberdigit | 数量保留位数 | int8 | 64 |  | √ | 0 | 数量保留位数 |
| 15 | fadjusttax | 是否开启税额调整 | bpchar | 1 |  | √ | '0' | 是否开启税额调整 |
| 16 | fhssplitamountenable | 是否开启 | bpchar | 1 |  | √ | '0' | 是否开启 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_split_hs_config |  | forg |
| 2 | pk_t_bdm_split_hs_config |  | fid |
