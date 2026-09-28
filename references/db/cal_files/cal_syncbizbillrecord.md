# 核算单同步日志-cal_syncbizbillrecord

## 核算单同步日志-多语言表 t_cal_servicelog_l

- **表名称：** 核算单同步日志-多语言表
- **表名：** t_cal_servicelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosereason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_servicelog_l |  | fpkid |
| 2 | idx_cal_servicelog_l |  | fid,flocaleid |

---

## 核算单同步日志-主表 t_cal_servicelog

- **表名称：** 核算单同步日志-主表
- **表名：** t_cal_servicelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 3 | fisclose | 是否关闭 | bpchar | 1 |  | √ | '0' | 是否关闭 |
| 4 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 5 | ftimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 6 | fbizentityobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fparammap | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | factionname | 功能名称 | varchar | 80 |  | √ | ' ' | 功能名称,枚举: SUBMIT :库存提交 UNSUBMIT :库存撤销 |
| 10 | fparammap_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 11 | fservicetype | 接口类型 | varchar | 80 |  | √ | ' ' | 接口类型,枚举: A :校验接口 B :业务接口 |
| 12 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 13 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fsuccess | 运行状态 | bpchar | 1 |  | √ | '0' | 运行状态,枚举: 0 :失败 1 :成功 2 :运行中 3 :业务失败 4 :系统失败 5 :警告 |
| 15 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 16 | fclosereason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 17 | fbizbillnumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_servicelog_bizbillid |  | fbizbillid |
| 2 | t_cal_servicelog_pkey |  | fid |
| 3 | idx_cal_servicelog_daorac |  | fexetime,fbookdate,forgid,factionname |
