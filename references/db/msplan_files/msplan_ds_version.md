# 数据版本-msplan_ds_version

## 子单据体-子表 t_msplan_dv_detail

- **表名称：** 子单据体-子表
- **表名：** t_msplan_dv_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fhisfilter | 历史过滤设置 | varchar | 255 |  | √ | ' ' | 历史过滤设置 |
| 2 | fhisstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :进行中 S :成功 F :失败 C :取消 |
| 3 | fhiscols_tag | 历史显示字段_详情 | text | 0 |  |  | null | 历史显示字段_详情 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fhisentity | 历史实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fhisfilter_tag | 历史过滤设置_详情 | text | 0 |  |  | null | 历史过滤设置_详情 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fhisstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fhisfinishtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fhissettings | 历史设置 | int8 | 64 |  | √ | 0 | [同步设置 msplan_ds_settings](../msplan_files/msplan_ds_settings.md) |
| 12 | fhiscols | 历史显示字段 | varchar | 255 |  | √ | ' ' | 历史显示字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dv_detail |  | fdetailid |
| 2 | idx_msplan_dv_detail |  | fentryid,fseq |

---

## 同步设置-多选基础资料表 t_msplan_dv_settings

- **表名称：** 同步设置-多选基础资料表
- **表名：** t_msplan_dv_settings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [同步设置 msplan_ds_settings](../msplan_files/msplan_ds_settings.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_dv_settings |  | fid |
| 2 | pk_t_msplan_dv_settings |  | fpkid |

---

## 数据版本-主表 t_msplan_dataversion

- **表名称：** 数据版本-主表
- **表名：** t_msplan_dataversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillstatusfield | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dataversion |  | fid |
| 2 | idx_msplan_dataversion |  | fnumber |

---

## 同步历史-子表 t_msplan_dv_hisentry

- **表名称：** 同步历史-子表
- **表名：** t_msplan_dv_hisentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivestatus | 生效状态 | varchar | 50 |  | √ | ' ' | 生效状态,枚举: A :激活 B :失效 D :数据已删除 |
| 3 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fuserfield | 版本修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsynclog_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 6 | fstartdatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fsynclog | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ffinishdatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdatetimefield | 版本修改时间 | timestamp | 0 |  |  | null | 版本修改时间 |
| 12 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: A :进行中 S :成功 F :失败 C :取消 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_dv_hisentry |  | fid,fseq |
| 2 | pk_t_msplan_dv_hisentry |  | fentryid |

---

## 子单据体-子表 t_msplan_dv_syncinfo

- **表名称：** 子单据体-子表
- **表名：** t_msplan_dv_syncinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | flogdetail_tag | 执行日志_详情 | text | 0 |  |  | null | 执行日志_详情 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | flogdetail | 执行日志 | varchar | 255 |  | √ | ' ' | 执行日志 |
| 6 | ftextfield | 表名 | varchar | 255 |  | √ | ' ' | 表名 |
| 7 | fdatacount | 同步行数 | int4 | 32 |  | √ | 0 | 同步行数 |
| 8 | fsyncentitytag | 标识 | varchar | 255 |  | √ | ' ' | 标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_dv_syncinfo |  | fentryid,fseq |
| 2 | pk_t_msplan_dv_syncinfo |  | fdetailid |

---

## 数据版本-多语言表 t_msplan_dataversion_l

- **表名称：** 数据版本-多语言表
- **表名：** t_msplan_dataversion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dataversion_l |  | fpkid |
| 2 | idx_msplan_dataversion_l |  | fid,flocaleid |
