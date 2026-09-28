# 商旅用车场景-er_trip_vehicle_setting

## 商旅用车场景-主表 t_er_trip_vehicle_setting

- **表名称：** 商旅用车场景-主表
- **表名：** t_er_trip_vehicle_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fapplysource | 审批数据来源 | varchar | 50 |  | √ | ' ' | 审批数据来源,枚举: 0 :无 er_tripreqbill :出差申请单 er_dailyvehiclebill :用车申请单 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 6 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 管控状态 | varchar | 50 |  | √ | ' ' | 管控状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fdatenum | 弹性天数 | int8 | 64 |  |  | null | 弹性天数 |
| 11 | fvehicletype | 用车类型 | varchar | 50 |  | √ | ' ' | 用车类型,枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_vehicle_setting |  | fid |
| 2 | idx_er_trip_vehicle_setting_fapplysource |  | fapplysource |

---

## 商旅用车场景-多语言表 t_er_trip_vehicle_setting_l

- **表名称：** 商旅用车场景-多语言表
- **表名：** t_er_trip_vehicle_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_vehicle_setting_l |  | fpkid |
