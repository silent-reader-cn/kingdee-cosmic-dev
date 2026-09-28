# 生态接入监听-msisv_ecologicmonitor

## 生态接入监听-主表 t_msisv_ecologicmonitor

- **表名称：** 生态接入监听-主表
- **表名：** t_msisv_ecologicmonitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmonitorobj | 监听对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [生态接入监听分类 msisv_monitortype](../msisv_files/msisv_monitortype.md) |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbizapp | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ffilterjson | 通用过滤json | varchar | 255 |  | √ | ' ' | 通用过滤json |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ffilterformula_tag | 通用过滤表达式_详情 | text | 0 |  |  | null | 通用过滤表达式_详情 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fmonitoroperation | 监听操作 | varchar | 50 |  | √ | ' ' | 监听操作,枚举: |
| 20 | ffilterjson_tag | 通用过滤json_详情 | text | 0 |  |  | null | 通用过滤json_详情 |
| 21 | ffilterformula | 通用过滤表达式 | varchar | 255 |  | √ | ' ' | 通用过滤表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msisv_ecomonitor_num |  | fnumber |
| 2 | pk_t_msisv_ecologicmonitor |  | fid |

---

## 监听行为-子表 t_msisv_actionentry

- **表名称：** 监听行为-子表
- **表名：** t_msisv_actionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :联合下推 B :关联更新 C :服务调用 |
| 3 | fpushaction | 联合下推 | int8 | 64 |  | √ | 0 | [联合下推 msisv_unionpush](../msisv_files/msisv_unionpush.md) |
| 4 | fserviceactionjson_tag | 服务调用json_详情 | text | 0 |  |  | null | 服务调用json_详情 |
| 5 | fclassname | fclassname | varchar | 50 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fserviceaction | 服务调用 | varchar | 50 |  | √ | ' ' | 服务调用 |
| 8 | fupdateaction | 关联更新 | int8 | 64 |  | √ | 0 | [关联更新 msisv_relateupdate](../msisv_files/msisv_relateupdate.md) |
| 9 | fdescription | fdescription | varchar | 50 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fserviceactionjson | 服务调用json | varchar | 255 |  | √ | ' ' | 服务调用json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msisv_actionentry_id |  | fid |
| 2 | pk_t_msisv_actionentry |  | fentryid |

---

## 生态接入监听-多语言表 t_msisv_ecologicmonitor_l

- **表名称：** 生态接入监听-多语言表
- **表名：** t_msisv_ecologicmonitor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msisv_ecologicmonitor_l_id |  | fid,flocaleid |
| 2 | pk_t_msisv_ecologicmonitor_l |  | fpkid |
