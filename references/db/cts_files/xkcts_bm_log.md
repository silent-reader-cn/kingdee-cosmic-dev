# 批量修改执行日志-xkcts_bm_log

## 单据信息-子表 t_xkbm_logentry

- **表名称：** 单据信息-子表
- **表名：** t_xkbm_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbilltime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fbillid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresult | 修改结果 | varchar | 50 |  | √ | ' ' | 修改结果,枚举: 1 :成功 2 :失败 3 :部分成功 4 :异常 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_logentry |  | fentryid |
| 2 | idx_bm_logentry_fid |  | fid,fseq |

---

## 批量修改执行日志-主表 t_xkbm_log

- **表名称：** 批量修改执行日志-主表
- **表名：** t_xkbm_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 批改状态 | varchar | 10 |  | √ | ' ' | 批改状态,枚举: 0 :未开始 1 :批改中 2 :已完成 |
| 3 | fmodifier | 批改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexcmsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 5 | fresult | 批改结果 | varchar | 50 |  | √ | ' ' | 批改结果,枚举: 1 :成功 2 :失败 3 :部分成功 4 :异常 |
| 6 | fexcmsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 7 | fbizobj | 业务对象编码 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 批改时间 | timestamp | 0 |  |  | null | 批改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_log |  | fid |
| 2 | idx_xkbm_log_obj |  | fbizobj |

---

## 字段信息-子表 t_xkbm_logdetail

- **表名称：** 字段信息-子表
- **表名：** t_xkbm_logdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foldvalue_tag | 修改前的ID或编码_详情 | text | 0 |  |  | null | 修改前的ID或编码_详情 |
| 2 | foldname_tag | 修改前的值_详情 | text | 0 |  |  | null | 修改前的值_详情 |
| 3 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | foldname | 修改前的值 | varchar | 255 |  | √ | ' ' | 修改前的值 |
| 5 | foldvalue | 修改前的ID或编码 | varchar | 255 |  | √ | ' ' | 修改前的ID或编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillentryseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 8 | fresult | 修改结果 | varchar | 50 |  | √ | ' ' | 修改结果,枚举: 1 :成功 2 :失败 |
| 9 | ffailmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 10 | ffieldkey | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 11 | fnewvalue | 修改后的ID或编码 | varchar | 255 |  | √ | ' ' | 修改后的ID或编码 |
| 12 | fnewname_tag | 修改后的值_详情 | text | 0 |  |  | null | 修改后的值_详情 |
| 13 | ffailmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 14 | fbillentryid | 单据分录ID | varchar | 50 |  | √ | ' ' | 单据分录ID |
| 15 | fnewname | 修改后的值 | varchar | 255 |  | √ | ' ' | 修改后的值 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fnewvalue_tag | 修改后的ID或编码_详情 | text | 0 |  |  | null | 修改后的ID或编码_详情 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logdetail_fentryid |  | fentryid,fseq |
| 2 | pk_xkbm_logdetail |  | fdetailid |
