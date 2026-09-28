# 签收用户组-plm_plmdc_sign_group

## 签收用户组-主表 t_plmdc_sign_group

- **表名称：** 签收用户组-主表
- **表名：** t_plmdc_sign_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | freleaseid | 发布单ID | int8 | 64 |  | √ | 0 | 发布单ID |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | frecipientobjid | 接收者对象ID | varchar | 255 |  | √ | ' ' | 接收者对象ID |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_sgroup_resid |  | freleaseid |
| 2 | idx_plmdc_sign_group_fid |  | fnumber |
| 3 | pk_t_plmdc_sign_group |  | fid |

---

## 签收用户组-多语言表 t_plmdc_sign_group_l

- **表名称：** 签收用户组-多语言表
- **表名：** t_plmdc_sign_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_sign_group_l |  | fpkid |
| 2 | idx_plmdc_sign_group_l_fpkid |  | fid |

---

## 单据体-子表 t_plmdc_sign_group_entity

- **表名称：** 单据体-子表
- **表名：** t_plmdc_sign_group_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecipienttype | 接收者类型 | varchar | 50 |  | √ | ' ' | 接收者类型,枚举: usergroup :用户组 department :部门 role :角色 user :用户 |
| 3 | fuser | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fopendocright | 打开文档 | bpchar | 1 |  | √ | '0' | 打开文档 |
| 6 | fdowloaddocright | 下载文档 | bpchar | 1 |  | √ | '0' | 下载文档 |
| 7 | fsigntime | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 8 | fviewdocright | 查看文档 | bpchar | 1 |  | √ | '1' | 查看文档 |
| 9 | fviewpdfright | 浏览PDF | bpchar | 1 |  | √ | '0' | 浏览PDF |
| 10 | fviewlightright | 浏览轻量化 | bpchar | 1 |  | √ | '0' | 浏览轻量化 |
| 11 | fsignstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: unreceipted :待签收 partreceipted :部分签收 receipted :已签收 rejected :已拒签 noneedreceipted :无需签收 |
| 12 | fdowloadstepright | 下载STEP | bpchar | 1 |  | √ | '0' | 下载STEP |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fsignremark | 签收意见 | varchar | 2000 |  | √ | ' ' | 签收意见 |
| 15 | fdowloadpdfright | 下载PDF | bpchar | 1 |  | √ | '0' | 下载PDF |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_sign_group_entity |  | fdetailid |
| 2 | idx_plmdc_sgroup_e_user |  | fuser |
