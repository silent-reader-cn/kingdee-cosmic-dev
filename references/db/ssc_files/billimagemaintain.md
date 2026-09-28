# 影像映射维护-billimagemaintain

## 影像映射维护-主表 t_tk_billimagemap

- **表名称：** 影像映射维护-主表
- **表名：** t_tk_billimagemap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fimagestate | 影像状态 | bpchar | 1 |  | √ | ' ' | 影像状态,枚举: 0 :无影像 1 :上传影像中 2 :影像已就绪 3 :退回重扫 4 :影像重传 5 :废弃 |
| 3 | fscanclientip | 影像扫描客户端IP | varchar | 50 |  | √ | ' ' | 影像扫描客户端IP |
| 4 | feasid | feasid | varchar | 50 |  | √ | ' ' |  |
| 5 | fnextscanuserid | 下一代扫描员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fscantime | 扫描时间 | timestamp | 0 |  |  | null | 扫描时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fupdateaccount | 修改人账号 | varchar | 50 |  | √ | ' ' | 修改人账号 |
| 9 | fimageurl | 影像URL | varchar | 255 |  |  | null | 影像URL |
| 10 | fpagecount | 影像张数 | int8 | 64 |  | √ | 0 | 影像张数 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmaterialstate | 实物状态 | varchar | 2 |  | √ | ' ' | 实物状态,枚举: 0 :无 1 :共享中心接收 2 :稽核通过 3 :实物稽核通过 4 :实物稽核不通过 |
| 13 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatorname | 创建人姓名 | varchar | 50 |  | √ | ' ' | 创建人姓名 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fcreatororgid | 提单人公司id | varchar | 50 |  | √ | ' ' | 提单人公司id |
| 18 | fsscunitid | 扫描点 | int8 | 64 |  | √ | 0 | [扫描点 bos_sscunitlist](../sys_files/bos_sscunitlist.md) |
| 19 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 20 | fbillnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 22 | fbillfieldmap | 单据字段映射 | varchar | 500 |  | √ | ' ' | 单据字段映射 |
| 23 | fcreatoraccount | 创建人账号 | varchar | 50 |  | √ | ' ' | 创建人账号 |
| 24 | fsimplename | 简称 | varchar | 50 |  | √ | ' ' | 简称 |
| 25 | fscanuserid | 影像扫描用户ID | varchar | 50 |  | √ | ' ' | 影像扫描用户ID |
| 26 | fwfprocessingid | 工作流实例ID | varchar | 50 |  | √ | ' ' | 工作流实例ID |
| 27 | fbillid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 29 | forgname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 30 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 31 | fneedimagescan | 是否需要影像扫描 | bpchar | 1 |  | √ | '1' | 是否需要影像扫描,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_imagemap_imagenum |  | fimagenumber |
| 2 | idx_ssc_imagemap_imagebillid |  | fbillid |
| 3 | t_tk_billimagemap_pkey |  | fid |
| 4 | idx_ssc_imagemap_modifytime |  | fmodifytime |
| 5 | idx_ssc_imagemap_scanuserid |  | fscanuserid |

---

## 影像映射维护-多语言表 t_tk_billimagemap_l

- **表名称：** 影像映射维护-多语言表
- **表名：** t_tk_billimagemap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_billimagel_locale |  | fid,flocaleid |
| 2 | t_tk_billimagemap_l_pkey |  | fpkid |
