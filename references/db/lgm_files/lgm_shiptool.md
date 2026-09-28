# 运输工具档案-lgm_shiptool

## 运输工具档案-多语言表 t_lgm_shiptool_l

- **表名称：** 运输工具档案-多语言表
- **表名：** t_lgm_shiptool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shiptool_l |  | fpkid |
| 2 | idx_lgm_shiptool_l_id |  | fid,flocaleid |

---

## 运输工具档案-主表 t_lgm_shiptool

- **表名称：** 运输工具档案-主表
- **表名：** t_lgm_shiptool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flasttracker | 追踪更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 6 | fupdator | 更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fnamestd | 运输工具号 | varchar | 255 |  | √ | ' ' | 运输工具号 |
| 8 | fcallsign | 呼号 | varchar | 50 |  | √ | ' ' | 呼号 |
| 9 | fimo | IMO | varchar | 50 |  | √ | ' ' | IMO |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | ftranstype | 运输方式 | varchar | 50 |  | √ | ' ' | 运输方式,枚举: ship :海运 |
| 15 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 16 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | flasttrackuptime | 追踪更新时间 | timestamp | 0 |  |  | null | 追踪更新时间 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fshiptype | 船舶类型 | varchar | 50 |  | √ | ' ' | 船舶类型 |
| 20 | fshipid | MMSI | varchar | 255 |  | √ | ' ' | MMSI |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shiptool |  | fid |
| 2 | idx_lgm_shiptool_shipid |  | fshipid,ftranstype |
| 3 | idx_lgm_shiptool_fnamestd |  | fnamestd |
