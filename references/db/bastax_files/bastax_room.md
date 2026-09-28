# 房间基础信息-bastax_room

## 房间基础信息-主表 t_bastax_room

- **表名称：** 房间基础信息-主表
- **表名：** t_bastax_room

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 房间名称 | varchar | 50 |  | √ | ' ' | 房间名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fstage | 分期 | int8 | 64 |  | √ | 0 | [分期信息 bastax_stage](../bastax_files/bastax_stage.md) |
| 6 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbuilding | 楼栋 | int8 | 64 |  | √ | 0 | [楼栋信息 bastax_building](../bastax_files/bastax_building.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ftaxproject | 税务项目 | int8 | 64 |  | √ | 0 | [税务项目信息 bastax_taxproject](../bastax_files/bastax_taxproject.md) |
| 10 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 11 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcetype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :excel导入 |
| 18 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 19 | froomno | 房间号 | varchar | 50 |  | √ | ' ' | 房间号 |
| 20 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 21 | farea | 地上可售计容面积 | numeric | 23 | 10 | √ | 0 | 地上可售计容面积 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 房间编码 | varchar | 50 |  | √ | ' ' | 房间编码 |
| 24 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bastax_room_master |  | fmasterid |
| 2 | idx_t_bastax_room_createorg |  | fcreateorgid |
| 3 | pk_bastax_room |  | fid |

---

## 房间基础信息-多语言表 t_bastax_room_l

- **表名称：** 房间基础信息-多语言表
- **表名：** t_bastax_room_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 房间名称 | varchar | 50 |  | √ | ' ' | 房间名称 |
| 3 | froomno | froomno | varchar | 50 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_room_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_room_l |  | fpkid |
