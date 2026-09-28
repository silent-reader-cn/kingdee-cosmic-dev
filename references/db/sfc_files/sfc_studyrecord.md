# 学习记录(废弃)-sfc_studyrecord

## 学习记录(废弃)-主表 t_sfc_studyrecord

- **表名称：** 学习记录(废弃)-主表
- **表名：** t_sfc_studyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispass | 考试通过 | bpchar | 1 |  | √ | '0' | 考试通过 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstudycontent | 学习内容编码 | int8 | 64 |  | √ | 0 | [学习内容(废弃) sfc_studycontent](../sfc_files/sfc_studycontent.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fuser | 员工工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdatasrc | 数据来源 | int8 | 64 |  | √ | 0 | [数据来源(废弃) sfc_datasrc](../sfc_files/sfc_datasrc.md) |
| 9 | fexpstudydate | 学习有效截止时间 | timestamp | 0 |  |  | null | 学习有效截止时间 |
| 10 | fstudynumber | 学习编码 | varchar | 50 |  | √ | ' ' | 学习编码 |
| 11 | fstudydate | 学习时间 | timestamp | 0 |  |  | null | 学习时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_studyrecord |  | fid |
| 2 | t_sfc_studyrecord_fuser_idx |  | fuser |
