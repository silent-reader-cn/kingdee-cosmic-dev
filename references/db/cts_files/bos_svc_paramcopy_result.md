# 参数复制结果-bos_svc_paramcopy_result

## 参数复制结果-主表 t_svc_paramcopy_result

- **表名称：** 参数复制结果-主表
- **表名：** t_svc_paramcopy_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fsourceorg | 源组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fstart | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcopyapp | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fdescription | 说明 | varchar | 255 |  |  | null | 说明 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcopystatus | 复制进度 | bpchar | 1 |  | √ | ' ' | 复制进度,枚举: 0 :复制成功 1 :复制失败 |
| 13 | fcopybasedataid | 参数复制基础资料 | int8 | 64 |  | √ | 0 | [参数复制 bos_svc_parametercopy](../cts_files/bos_svc_parametercopy.md) |
| 14 | fend | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 15 | fbillno | 任务编码 | varchar | 30 |  | √ | ' ' | 任务编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_svc_paramcopy_result |  | fbillno |
| 2 | pk_t_svc_paramcopy_result |  | fid |

---

## 目标组织-多选基础资料表 t_svc_paramcopy_res_torg

- **表名称：** 目标组织-多选基础资料表
- **表名：** t_svc_paramcopy_res_torg

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
| 1 | idx_svc_paramcpy_res_torg |  | fid |
| 2 | pk_t_svc_paramcopy_res_torg |  | fpkid |
