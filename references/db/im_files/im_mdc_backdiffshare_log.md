# 领料差异分摊详情（废弃）-im_mdc_backdiffshare_log

## 单据体-子表 t_im_mdc_difsharelogentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_difsharelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassigndetail | fassigndetail | varchar | 50 |  | √ | ' ' |  |
| 3 | fsharedetail | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fshauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fdiffsharef7 | 倒冲差异分摊F7 | int8 | 64 |  | √ | 0 | [领料差异分摊F7 im_mdc_backdiffshare_f7](../im_files/im_mdc_backdiffshare_f7.md) |
| 8 | fshmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_difsharelog_a |  | fid |
| 2 | pk_im_mdc_difsharelogentry |  | fentryid |

---

## 领料差异分摊详情（废弃）-主表 t_im_mdc_difsharelog

- **表名称：** 领料差异分摊详情（废弃）-主表
- **表名：** t_im_mdc_difsharelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmftorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | findatestart | 入库日期.开始 | timestamp | 0 |  |  | null | 入库日期.开始 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdiffshareid | 倒冲差异分摊id | int8 | 64 |  | √ | 0 | 倒冲差异分摊id |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finvdate | finvdate | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | finvorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fsharebillno | 分摊单据编号 | varchar | 50 |  | √ | ' ' | 分摊单据编号 |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | findateend | 入库日期.结束 | timestamp | 0 |  |  | null | 入库日期.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_difsharelog |  | fdiffshareid |
| 2 | pk_im_mdc_difsharelog |  | fid |
