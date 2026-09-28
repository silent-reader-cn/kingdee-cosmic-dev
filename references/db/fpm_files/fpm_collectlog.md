# 采集日志-fpm_collectlog

## 单据体-子表 t_fpm_collect_execrecord

- **表名称：** 单据体-子表
- **表名：** t_fpm_collect_execrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebillnumber | 业务来源单据编码 | varchar | 50 |  | √ | ' ' | 业务来源单据编码 |
| 3 | fexecuteresult | 是否成功 | bpchar | 1 |  | √ | ' ' | 是否成功 |
| 4 | fsourcebilleid | 业务来源单据分录ID | int8 | 64 |  | √ | 0 | 业务来源单据分录ID |
| 5 | fsourcebillid | 来源业务单据id | int8 | 64 |  | √ | 0 | 来源业务单据id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fexecdetail_tag | 执行详情_详情 | text | 0 |  |  | null | 执行详情_详情 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fexecdetail | 执行详情 | text | 0 |  |  | null | 执行详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_collect_execrecord_org |  | fsourcebilleid |
| 2 | pk_t_fpm_collect_execrecord |  | fentryid |

---

## 采集日志-主表 t_fpm_collectlog

- **表名称：** 采集日志-主表
- **表名：** t_fpm_collectlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ferrorinfo | 采集中断异常 | text | 0 |  |  | null | 采集中断异常 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcollectcaseid | 采集方案 | int8 | 64 |  | √ | 0 | [业务数据采集方案 fpm_smartcollect](../fpm_files/fpm_smartcollect.md) |
| 6 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 7 | fexecutedetail | 执行详情 | varchar | 255 |  | √ | ' ' | 执行详情 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsourcebill | 来源业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fgathercount | 采集总量 | int4 | 32 |  | √ | 0 | 采集总量 |
| 12 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ferrorinfo_tag | 采集中断异常_详情 | text | 0 |  |  | null | 采集中断异常_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_collectlog_billno |  | fbillno |
| 2 | pk_t_fpm_collectlog |  | fid |

---

## 适用组织-多选基础资料表 t_fpm_loggerapplyorg

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_fpm_loggerapplyorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fpm_loggerapplyorg_fid |  | fid |
| 2 | pk_t_fpm_loggerapplyorg |  | fpkid |
