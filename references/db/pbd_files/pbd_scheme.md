# 供应商管控配置-pbd_scheme

## 供应商管控配置-主表 t_pbd_controlscheme

- **表名称：** 供应商管控配置-主表
- **表名：** t_pbd_controlscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffiltergridtext | 受控条件 | text | 0 |  |  | null | 受控条件 |
| 3 | ftooltips | 提示信息 | varchar | 512 |  | √ | ' ' | 提示信息 |
| 4 | ffilterpage_tag | 管控条件配置后台_详情 | text | 0 |  |  | null | 管控条件配置后台_详情 |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fcontrolmode | 管控强度 | bpchar | 1 |  | √ | ' ' | 管控强度,枚举: 1 :预警提示 2 :终止操作 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fdefaultclass | 实现插件 | varchar | 255 |  | √ | ' ' | 实现插件 |
| 12 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fcontroltypeid | 管控要素 | int8 | 64 |  | √ | 0 | [管控要素 pbd_controltype](../pbd_files/pbd_controltype.md) |
| 16 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 19 | ffiltergridtext_tag | 受控条件_详情 | text | 0 |  |  | null | 受控条件_详情 |
| 20 | ffilterpage | 管控条件配置后台 | varchar | 100 |  | √ | ' ' | 管控条件配置后台 |
| 21 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fbillentityid | 业务单据 | int8 | 64 |  | √ | 0 | [单据注册 pbd_billregister](../pbd_files/pbd_billregister.md) |
| 24 | foperationfield | 单据操作 | varchar | 50 |  | √ | ' ' | 单据操作,枚举: |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_controlscheme |  | fid |
| 2 | idx_pbd_controlscheme_bill |  | fbillentityid |

---

## 供应商管控配置-多语言表 t_pbd_controlscheme_l

- **表名称：** 供应商管控配置-多语言表
- **表名：** t_pbd_controlscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ftooltips | 提示信息 | varchar | 512 |  | √ | ' ' | 提示信息 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_controlscheme_l |  | fpkid |
| 2 | idx_pbd_controlscheme_l_fid |  | fid,flocaleid |
