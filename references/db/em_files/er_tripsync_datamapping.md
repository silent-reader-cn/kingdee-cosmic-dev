# 商旅集成关联数据映射-er_tripsync_datamapping

## 商旅集成关联数据映射-主表 t_er_tripsync_datamapping

- **表名称：** 商旅集成关联数据映射-主表
- **表名：** t_er_tripsync_datamapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foutdatanumber | 外部数据编码 | varchar | 100 |  | √ | ' ' | 外部数据编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | finnerdataid | 内部数据ID | int8 | 64 |  | √ | 0 | 内部数据ID |
| 7 | foutdataid | 外部数据ID | int8 | 64 |  | √ | 0 | 外部数据ID |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fserver | 商旅服务商 | varchar | 30 |  | √ | ' ' | 商旅服务商,枚举: DIDI :滴滴 MEITUAN :美团 GAODE :高德 MEIYA :美亚 ALIQIYEMA :阿里企业码 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 内部数据编号 | varchar | 200 |  | √ | ' ' | 内部数据编号 |
| 14 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: bos_org :组织 bos_user :人员 er_tripreq :出差申请单 er_city :商旅城市 er_dailyvehiclebill :用车申请单 er_dailyapplybill :费用申请单 er_dailyapplybill_rule :费用申请单_规则 er_dailyapplybill_quota :费用申请单_额度 er_tripreqbill :出差申请单 er_tripreqbill_rule :出差申请单_规则 er_tripreqbill_quota :出差申请单_额度 er_tripreqbill_inter :全球出差申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripsync_datamapping |  | fid |
| 2 | idx_datamapping_innerdataid |  | finnerdataid |
| 3 | idx_datamapping_outdataid |  | foutdataid |

---

## 商旅集成关联数据映射-多语言表 t_er_tripsync_datamapping_l

- **表名称：** 商旅集成关联数据映射-多语言表
- **表名：** t_er_tripsync_datamapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 内部数据名称 | varchar | 100 |  | √ | ' ' | 内部数据名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_datamapping_l_id |  | fid,flocaleid |
| 2 | pk_t_er_tripsync_datamapping_l |  | fpkid |
