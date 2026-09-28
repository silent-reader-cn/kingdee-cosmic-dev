# 活动执行记录-ocmem_activityexec_record

## 单据体-子表 t_ocmem_activitytrackexec

- **表名称：** 单据体-子表
- **表名：** t_ocmem_activitytrackexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicture7 | 图片7 | varchar | 255 |  | √ | ' ' | 图片7 |
| 3 | fpicture6 | 图片6 | varchar | 255 |  | √ | ' ' | 图片6 |
| 4 | fpicture5 | 图片5 | varchar | 255 |  | √ | ' ' | 图片5 |
| 5 | ftracktime | 实际执行时间 | timestamp | 0 |  |  | null | 实际执行时间 |
| 6 | fpicture4 | 图片4 | varchar | 255 |  | √ | ' ' | 图片4 |
| 7 | fpicture3 | 图片3 | varchar | 255 |  | √ | ' ' | 图片3 |
| 8 | fpicture2 | 图片2 | varchar | 255 |  | √ | ' ' | 图片2 |
| 9 | fpicture1 | 图片1 | varchar | 255 |  | √ | ' ' | 图片1 |
| 10 | factivityplanld | 营销活动 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fdescription | 执行跟踪说明 | varchar | 500 |  | √ | ' ' | 执行跟踪说明 |
| 13 | ftrackuserid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frecordid | frecordid | int8 | 64 |  | √ | 0 |  |
| 15 | fnexttracktime | 下次跟踪时间 | timestamp | 0 |  |  | null | 下次跟踪时间 |
| 16 | fpicture8 | 图片8 | varchar | 255 |  | √ | ' ' | 图片8 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activitytrackexec |  | fid |
| 2 | idx_ocmem_activitytrackexec_01 |  | factivityplanld |

---

## 活动执行记录-主表 t_ocmem_actexecrecord

- **表名称：** 活动执行记录-主表
- **表名：** t_ocmem_actexecrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 标记 | varchar | 200 |  | √ | ' ' | 标记 |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | factplanid | 营销活动 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexecorgid | 执行部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frecordid | frecordid | int8 | 64 |  | √ | 0 | id |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | facttrackuserid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 执行编号 | varchar | 60 |  | √ | ' ' | 执行编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | frecordid | frecordid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_actexecrecord |  | frecordid |
| 2 | idx_ocmem_actexecrecord |  | factplanid |
