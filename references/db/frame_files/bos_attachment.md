# 附件面板实体-bos_attachment

## 附件面板实体-多语言表 t_bas_attachment_l

- **表名称：** 附件面板实体-多语言表
- **表名：** t_bas_attachment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachmentdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_attachment_l_pkey |  | fpkid |
| 2 | idx_bas_attachment_l |  | fid,flocaleid |

---

## 附件面板实体-主表 t_bas_attachment

- **表名称：** 附件面板实体-主表
- **表名：** t_bas_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemppageid | 临时PageID | varchar | 255 |  |  | null | 临时PageID |
| 3 | flocalid | 云之家文件存储地址 | varchar | 500 |  |  | ' ' | 云之家文件存储地址 |
| 4 | fmodifymen | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsort | 排序字段 | int4 | 32 |  |  | null | 排序字段 |
| 8 | fcreatemen | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbillno | 单据编号 | varchar | 255 |  |  | null | 单据编号 |
| 10 | fentryinterid | 单据体内码 | varchar | 50 |  |  | null | 单据体内码 |
| 11 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 13 | ffilesource | 文件来源 | int4 | 32 |  |  | 0 | 文件来源 |
| 14 | fentrykey | 单据体标识 | varchar | 50 |  |  | null | 单据体标识 |
| 15 | fdescription | 备注 | varchar | 255 |  |  | null | 备注 |
| 16 | fextname | 文件类型 | varchar | 30 |  |  | null | 文件类型 |
| 17 | fauditmen | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fattachmentpanel | 附件面板key | varchar | 80 |  |  | null | 附件面板key |
| 19 | fdragseq | 拖拽排序 | int8 | 64 |  | √ | 0 | 拖拽排序 |
| 20 | ffilestorage | ffilestorage | bpchar | 1 |  | √ | '0' |  |
| 21 | fattachmentsize | 大小（kb） | varchar | 50 |  |  | null | 大小（kb） |
| 22 | ffileid | url | varchar | 500 |  | √ | ' ' | url |
| 23 | faliasfilename | 别名 | varchar | 255 |  |  | null | 别名 |
| 24 | fnumber | 编码 | varchar | 50 |  |  | null | 编码 |
| 25 | fattachmentname | 文件名 | varchar | 255 |  |  | null | 文件名 |
| 26 | finterid | 单据内码 | varchar | 50 |  |  | null | 单据内码 |
| 27 | fbilltype | 单据类型 | varchar | 50 |  |  | null | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_attachment_pkey |  | fid |
| 2 | idx_bas_attachment_ffileid |  | ffileid |
| 3 | idx_bas_attachment |  | fnumber |
| 4 | idx_bas_attachment_02 |  | fbilltype,finterid |
| 5 | idx_bas_attachment_interid |  | finterid |
