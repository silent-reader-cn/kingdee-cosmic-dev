# 中途启用批号日志-im_midwayopenlotlog

## 单据体-子表 t_im_midwayopenlotlogbill

- **表名称：** 单据体-子表
- **表名：** t_im_midwayopenlotlogbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatebillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 3 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_midwayopenlotlogbill |  | fentryid |
| 2 | idx_im_midwayopenlotlogbill_fk |  | fid |

---

## 单据体-子表 t_im_midwayopenlotlogmat

- **表名称：** 单据体-子表
- **表名：** t_im_midwayopenlotlogmat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshelflifeunit | 保质期单位 | varchar | 50 |  | √ | ' ' | 保质期单位,枚举: day :日 month :月 year :年 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fshelflife | 保质期 | int8 | 64 |  | √ | 0 | 保质期 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenableshelf | 启用保质期管理 | bpchar | 1 |  | √ | '0' | 启用保质期管理 |
| 10 | fenablelot | 启用批号管理 | bpchar | 1 |  | √ | '0' | 启用批号管理 |
| 11 | fcalculationforenddate | 到期日计算方式 | varchar | 50 |  | √ | ' ' | 到期日计算方式,枚举: 0 :生产日期+保质期 1 :生产日期+保质期-1 2 :生产日期+保质期上个月的最后一天 |
| 12 | flotcoderuleid | 批号规则 | int8 | 64 |  | √ | 0 | [供应链编码规则 bd_lotcoderule](../sbd_files/bd_lotcoderule.md) |
| 13 | fcaldirection | 计算方向 | varchar | 50 |  | √ | ' ' | 计算方向,枚举: 1 :按生产日计算到期日 2 :按到期日计算生产日 3 :相互计算 4 :互不计算 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_midwayopenlotlogmat_fk |  | fid |
| 2 | pk_im_midwayopenlotlogmat |  | fentryid |

---

## 中途启用批号日志-主表 t_im_midwayopenlotlog

- **表名称：** 中途启用批号日志-主表
- **表名：** t_im_midwayopenlotlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_midwayopenlotlog |  | fid |
| 2 | idx_im_midwayopenlotlog_m0 |  | fbillno |
