# 打印向导记录-bos_prt_guide_record

## 打印向导记录-主表 t_svc_printguide_record

- **表名称：** 打印向导记录-主表
- **表名：** t_svc_printguide_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :新手向导 1 :表格向导 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | frnum | 引导次数 | int4 | 32 |  | √ | 0 | 引导次数 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_printguide_record |  | fid |
| 2 | idx_svc_printguide_u_t |  | fuserid,ftype |
