# 组合识别器文件-cvp_cls_file

## 组合识别器文件-主表 t_cvp_cls_fileinfo

- **表名称：** 组合识别器文件-主表
- **表名：** t_cvp_cls_fileinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpagenum | 总页数 | int4 | 32 |  | √ | 0 | 总页数 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffiletype | 文件类型 | varchar | 10 |  |  | ' ' | 文件类型 |
| 7 | fpreviewurl | 文件预览路径(图和pdf) | varchar | 1000 |  |  | ' ' | 文件预览路径(图和pdf) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | ffileurl | 文件持久化路径(原文件) | varchar | 1000 |  |  | ' ' | 文件持久化路径(原文件) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ffilename | 文件名称 | varchar | 200 |  |  | ' ' | 文件名称 |
| 13 | ffilesize | 文件大小 | int8 | 64 |  | √ | 0 | 文件大小 |
| 14 | fbillno | 单据编号 | varchar | 30 |  |  | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cvp_cls_fileinfo |  | fbillno,fbillstatus |
| 2 | pk_t_cvp_cls_fileinfo |  | fid |
