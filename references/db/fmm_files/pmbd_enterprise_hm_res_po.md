# 企业人力资源池-pmbd_enterprise_hm_res_po

## 部门分录-子表 t_pmbd_hm_res_userp

- **表名称：** 部门分录-子表
- **表名：** t_pmbd_hm_res_userp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgstructureid | 组织结构 | int8 | 64 |  | √ | 0 | [行政组织结构 bos_adminorg_structure](../base_files/bos_adminorg_structure.md) |
| 3 | fispartjob | 兼职 | bpchar | 1 |  | √ | '0' | 兼职 |
| 4 | fdepcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdepcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsuperiorid | 直接上级 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fisincharge | 负责人 | bpchar | 1 |  | √ | '0' | 负责人 |
| 9 | fdepmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdepmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_hm_res_userp |  | fentryid |
| 2 | idx_pmbd_hm_fid |  | fid |
| 3 | idx_pmbd_hm_fseq |  | fseq |

---

## 项目信息分录-子表 t_pmbd_hm_res_project

- **表名称：** 项目信息分录-子表
- **表名：** t_pmbd_hm_res_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fsourcename | 源单名称 | varchar | 5 |  | √ | ' ' | 源单名称,枚举: 1001 :项目人力资源策划 1002 :项目团队 |
| 4 | fprojectmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprojecthmrespl | 源单单据内码 | int8 | 64 |  | √ | 0 | 源单单据内码 |
| 7 | fprojectcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fteamentryentityid | 团队内码 | int8 | 64 |  | √ | 0 | 团队内码 |
| 10 | fprojectcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | frole | 角色名称 | varchar | 50 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 12 | faddproducttime | 加入项目时间 | timestamp | 0 |  |  | null | 加入项目时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_hm_res_project |  | fentryid |
| 2 | idx_pmbd_hm_fseq4 |  | fseq |
| 3 | idx_pmbd_hm_fid4 |  | fid |

---

## 企业人力资源池-主表 t_pmbd_ep_hm_res_po

- **表名称：** 企业人力资源池-主表
- **表名：** t_pmbd_ep_hm_res_po

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fgender | 性别 | varchar | 5 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 : |
| 6 | fdatasources | 数据来源 | varchar | 5 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :引入系统人员 C :引入制造人员 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | favatar | 人员头像 | varchar | 255 |  | √ | ' ' | 人员头像 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdatasourcesid | 数据来源ID | int8 | 64 |  | √ | 0 | 数据来源ID |
| 15 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fusertype | 类型 | int8 | 64 |  | √ | 0 | [人员类型 bos_usertype](../base_files/bos_usertype.md) |
| 17 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_ep_hm_res_po |  | fid |
| 2 | idx_pmbd_ep_fcreatetime |  | fcreatetime |
| 3 | idx_pmbd_ep_fnumber |  | fnumber |

---

## 联系方式分录-子表 t_pmbd_hm_res_usercontact

- **表名称：** 联系方式分录-子表
- **表名：** t_pmbd_hm_res_usercontact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcontactcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcontact | 联系方式 | varchar | 255 |  | √ | ' ' | 联系方式 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcontacttypeid | 类型 | int8 | 64 |  | √ | 0 | [人员联系方式类型 bos_user_contacttype](../base_files/bos_user_contacttype.md) |
| 8 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 9 | fcontactmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcontactmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_hm_res_usercontact |  | fentryid |
| 2 | idx_pmbd_hm_fseq1 |  | fseq |
| 3 | idx_pmbd_hm_fid1 |  | fid |

---

## 企业人力资源池-多语言表 t_pmbd_ep_hm_res_po_l

- **表名称：** 企业人力资源池-多语言表
- **表名：** t_pmbd_ep_hm_res_po_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_ep_hm_res_po_l |  | fpkid |
| 2 | idx_pmbd_epl_fname |  | fname |
| 3 | idx_pmbd_epl_fid |  | fid,flocaleid |

---

## 部门分录-多语言表 t_pmbd_hm_res_userp_l

- **表名称：** 部门分录-多语言表
- **表名：** t_pmbd_hm_res_userp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_hm_res_userp_l |  | fpkid |
| 2 | idx_pmbd_hml_fposition |  | fposition |
| 3 | idx_pmbd_hml_fentryid |  | fentryid,flocaleid |

---

## 角色信息分录-子表 t_pmbd_hm_res_role

- **表名称：** 角色信息分录-子表
- **表名：** t_pmbd_hm_res_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstandardtime | 标准时间量（H/天） | numeric | 23 | 2 | √ | 0 | 标准时间量（H/天） |
| 3 | frolecreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fserviceprice | 服务价格（H） | numeric | 23 | 2 | √ | 0 | 服务价格（H） |
| 5 | frolemodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fmainrole | 主要角色 | bpchar | 1 |  | √ | '0' | 主要角色 |
| 7 | froleid | 角色编码 | varchar | 50 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 8 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | frolecreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fcostprice | 成本价格（H） | numeric | 23 | 2 | √ | 0 | 成本价格（H） |
| 12 | fstandardmaxtime | 标准时间最大量（H/天） | numeric | 23 | 2 | √ | 0 | 标准时间最大量（H/天） |
| 13 | frolemodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_hm_fseq2 |  | fseq |
| 2 | pk_pmbd_hm_res_role |  | fentryid |
| 3 | idx_pmbd_hm_fid2 |  | fid |

---

## 资质信息分录-子表 t_pmbd_hm_res_qation

- **表名称：** 资质信息分录-子表
- **表名：** t_pmbd_hm_res_qation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 3 | fqualificatcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fqualificationmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fqualifications | 人员资质 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 mpdm_qualifications](../mpdm_files/mpdm_qualifications.md) |
| 7 | fqualificationcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fgradelevel | 技能等级 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_gradelevel](../mpdm_files/mpdm_gradelevel.md) |
| 9 | fworktype | 工种 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 mpdm_worktype](../mpdm_files/mpdm_worktype.md) |
| 10 | fcrenumber | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 11 | feffectivedate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 12 | fclosingdate | 截止时间 | timestamp | 0 |  |  | null | 截止时间 |
| 13 | fveridate | 验证时间 | timestamp | 0 |  |  | null | 验证时间 |
| 14 | fqualificatiomodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fisdefworktype | 默认工种 | bpchar | 1 |  | √ | '0' | 默认工种 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_hm_fseq3 |  | fseq |
| 2 | pk_pmbd_hm_res_qation |  | fentryid |
| 3 | idx_pmbd_hm_fid3 |  | fid |
