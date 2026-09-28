# 座位等级设置-er_seatgradestd

## 座位等级设置-多语言表 t_er_seatgrade_l

- **表名称：** 座位等级设置-多语言表
- **表名：** t_er_seatgrade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseatgrade | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_seatgrade_l_id |  | fid,flocaleid |
| 2 | t_er_seatgrade_l_pkey |  | fpkid |

---

## 座位等级设置-主表 t_er_seatgrade

- **表名称：** 座位等级设置-主表
- **表名：** t_er_seatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 差旅项目属性 | int8 | 64 |  | √ | 0 | [差旅项目属性 er_vehicle](../em_files/er_vehicle.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseatgrade | fseatgrade | varchar | 100 |  | √ | ' ' |  |
| 6 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 7 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 14 | foutattribute | 映射发票识别座位等级 | varchar | 255 |  | √ | ' ' | 映射发票识别座位等级 |
| 15 | fattribute | 属性 | varchar | 30 |  | √ | ' ' | 属性,枚举: 2 :飞机 4 :火车 7 :轮船 3 :汽车 6 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_seatgrade_number |  | fnumber |
| 2 | t_er_seatgrade_pkey |  | fid |
| 3 | idx_t_er_seatgrade_attrbt |  | fattribute |
| 4 | idx_t_er_seatgrade_seat |  | fseatgrade |
