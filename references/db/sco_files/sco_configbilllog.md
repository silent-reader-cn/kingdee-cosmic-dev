# 配置方案变更日志-sco_configbilllog

## 单据体-子表 t_sco_configlog_ruleentry

- **表名称：** 单据体-子表
- **表名：** t_sco_configlog_ruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostbojectfield | 成本核算对象值 | varchar | 255 |  | √ | ' ' | 成本核算对象值 |
| 3 | fobjchangefield | 源单字段值 | varchar | 255 |  | √ | ' ' | 源单字段值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_clogruleentry |  | fid |
| 2 | pk_sco_configlog_ruleentry |  | fentryid |

---

## 配置方案变更日志-主表 t_sco_configbilllog

- **表名称：** 配置方案变更日志-主表
- **表名：** t_sco_configbilllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fafterfilter_tag | 变更后数据范围_详情 | text | 0 |  |  | null | 变更后数据范围_详情 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fsourcebill | 源单 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcostbillid | 成本单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fafterfilter | 变更后数据范围 | varchar | 2000 |  | √ | ' ' | 变更后数据范围 |
| 14 | fbeforefilter_tag | 变更前数据范围_详情 | text | 0 |  |  | null | 变更前数据范围_详情 |
| 15 | fcount | 变更次数 | int8 | 64 |  | √ | 0 | 变更次数 |
| 16 | fbillno | 配置单编号 | varchar | 255 |  | √ | ' ' | 配置单编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbeforefilter | 变更前数据范围 | varchar | 2000 |  | √ | ' ' | 变更前数据范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_configbilllog |  | fid |
| 2 | idx_sco_configbilllog |  | fbillno,forgid,fappnum |

---

## 单据体-子表 t_sco_configlog_mapentry

- **表名称：** 单据体-子表
- **表名：** t_sco_configlog_mapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedvalue | 源单字段值 | varchar | 1000 |  | √ | ' ' | 源单字段值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: 0 :新增 1 :修改 2 :删除 |
| 5 | fvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostfield | 成本字段值 | varchar | 255 |  | √ | ' ' | 成本字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_configlog_mapentry |  | fentryid |
| 2 | idx_sco_clogmapentry |  | fid |
