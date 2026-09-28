# 文件清理-ysq_process_file_clean

## 文件清理-主表 tk_ysq_process_file_clean

- **表名称：** 文件清理-主表
- **表名：** tk_ysq_process_file_clean

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_proc_code | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_ysq_integerfield | fk_ysq_integerfield | int8 | 64 |  |  | null |  |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_ysq_file_type | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: doc :Word docx :Word xls :Excel xlsx :Excel csv :Excel pptx :PPT txt :文本文件 pdf :Pdf png :图片 jpg :图片 jpeg :图片 bmp :图片 rar :压缩文件 zip :压缩文件 |
| 9 | fk_ysq_file_ids | 文件id集合 | varchar | 2000 |  | √ | ' ' | 文件id集合 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fk_ysq_proc_name | 流程名 | varchar | 50 |  | √ | ' ' | 流程名 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_ysq_user_name | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 15 | fk_ysq_file_size | 文件所占空间 | varchar | 200 |  | √ | ' ' | 文件所占空间 |
| 16 | fk_ysq_file_count | 文件数量 | int8 | 64 |  |  | null | 文件数量 |
| 17 | fk_ysq_cur_org_name | 组织 | varchar | 50 |  | √ | ' ' | 组织 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fk_ysq_file_create_type | 文件来源 | varchar | 50 |  | √ | ' ' | 文件来源,枚举: 0 :页面上传 1 :设计器上传 2 :机器人上传 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_process_file_clean |  | fid |
