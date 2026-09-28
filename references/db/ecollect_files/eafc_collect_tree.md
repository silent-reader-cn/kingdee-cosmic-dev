# 采集页面树形单据体-eafc_collect_tree

## 采集页面树形单据体-主表 tk_eafc_collect_tree

- **表名称：** 采集页面树形单据体-主表
- **表名：** tk_eafc_collect_tree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_image_no | 关联影像编号 | varchar | 50 |  | √ | ' ' | 关联影像编号 |
| 3 | fk_eafc_bill_maker | 制单人 | varchar | 50 |  | √ | ' ' | 制单人 |
| 4 | fk_eafc_file_suffix | 文件后缀 | varchar | 10 |  | √ | ' ' | 文件后缀 |
| 5 | fk_eafc_file_size | 文件尺寸 | int8 | 64 |  |  | null | 文件尺寸 |
| 6 | fk_fpy_file_repeat_id_tag | 文件重复id_详情 | text | 0 |  |  | null | 文件重复id_详情 |
| 7 | fk_eafc_original_file_url | 源文件url | varchar | 1000 |  | √ | ' ' | 源文件url |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fk_eafc_node_name | 节点名称 | varchar | 80 |  | √ | ' ' | 节点名称 |
| 10 | fk_eafc_createdate | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fk_eafc_bill_creater | 制单人 | varchar | 30 |  | √ | ' ' | 制单人 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fk_eafc_arcorg | 全宗名称 | int8 | 64 |  |  | null | [归档体系_旧 eafc_org](../esyset_files/eafc_org.md) |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fk_eafc_label_param | 标签参数 | varchar | 2000 |  | √ | ' ' | 标签参数 |
| 17 | fk_eafc_bill_poster | 过账人 | varchar | 30 |  | √ | ' ' | 过账人 |
| 18 | fk_eafc_collect_type | 采集方式 | varchar | 50 |  | √ | ' ' | 采集方式,枚举: 1 :本地上传 2 :扫描 3 :同步 |
| 19 | fk_eafc_archive_entryid | 凭证册id | int8 | 64 |  |  | null | 凭证册id |
| 20 | fk_eafc_node_no | 节点编号 | varchar | 50 |  | √ | ' ' | 节点编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fk_eafc_import_format | 导入格式 | varchar | 50 |  | √ | ' ' | 导入格式,枚举: 1 :单页PDF文件导入 2 :多页PDF文件导入 |
| 23 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fk_eafc_bill_reviewer | 复核人 | varchar | 30 |  | √ | ' ' | 复核人 |
| 25 | fk_eafc_eafc_file_name | 源文件名 | varchar | 100 |  | √ | ' ' | 源文件名 |
| 26 | fk_eafc_file_detail_id | 文件详情id | varchar | 255 |  | √ | ' ' | 文件详情id |
| 27 | fk_eafc_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 28 | fk_eafc_voucher_no | 凭证编号 | varchar | 30 |  | √ | ' ' | 凭证编号 |
| 29 | fk_eafc_bill_auditor | 审核人 | varchar | 30 |  | √ | ' ' | 审核人 |
| 30 | fk_eafc_archive_batch_no | 档案批次号 | varchar | 50 |  | √ | ' ' | 档案批次号 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fk_eafc_archive_type | 档案类型 | varchar | 50 |  | √ | ' ' | 档案类型,枚举: 1 :封面 2 :凭证 3 :附件 4 :发票 5 :单据 |
| 33 | fk_eafc_file_status | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 0 :正常 1 :识别错误 2 :数据重复 3 :必填字段缺失 4 :未匹配到数据 5 :文件名称不合规 6 :凭证中存在相同的文件 |
| 34 | fk_eafc_node_level | 节点的层级 | int8 | 64 |  |  | null | 节点的层级 |
| 35 | fk_eafc_archiveid | 档案id | int8 | 64 |  |  | null | 档案id |
| 36 | fk_eafc_bill_type | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 37 | fk_eafc_bill_amount | 影像单据金额 | numeric | 23 | 2 | √ | 0 | 影像单据金额 |
| 38 | fk_fpy_file_repeat_id | 文件重复id | varchar | 255 |  | √ | ' ' | 文件重复id |
| 39 | fk_eafc_creater | 采集人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fk_eafc_file_url | 展示文件url | varchar | 1000 |  | √ | ' ' | 展示文件url |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fk_eafc_apply_date | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 44 | fk_eafc_parentid | 父节点id | varchar | 30 |  | √ | ' ' | 父节点id |
| 45 | fk_eafc_long_number | 节点的长编码 | varchar | 300 |  | √ | ' ' | 节点的长编码 |
| 46 | fk_eafc_bill_bookkeeper | 记账人 | varchar | 30 |  | √ | ' ' | 记账人 |
| 47 | fk_eafc_file_detail_id_tag | 文件详情id_详情 | text | 0 |  |  | null | 文件详情id_详情 |
| 48 | fk_eafc_image_bill_no | 影像单据编号 | varchar | 50 |  | √ | ' ' | 影像单据编号 |
| 49 | fk_eafc_file_seq | 文件顺序 | int8 | 64 |  |  | null | 文件顺序 |
| 50 | fk_eafc_file_upload_seq | 文件上传顺序 | int8 | 64 |  |  | null | 文件上传顺序 |
| 51 | fk_eafc_is_leaf | 是否为叶子节点 | varchar | 50 |  | √ | ' ' | 是否为叶子节点,枚举: 0 :否 1 :是 |
| 52 | fk_eafc_file_hash | 文件的hash值 | varchar | 100 |  | √ | ' ' | 文件的hash值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_collect_tree |  | fid |
