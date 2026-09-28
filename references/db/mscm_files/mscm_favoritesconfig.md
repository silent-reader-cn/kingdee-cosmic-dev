# 移动供应链_用户收藏夹-mscm_favoritesconfig

## 移动供应链_用户收藏夹-主表 t_mscm_favorites

- **表名称：** 移动供应链_用户收藏夹-主表
- **表名：** t_mscm_favorites

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftype | 收藏类型 | varchar | 40 |  | √ | ' ' | 收藏类型,枚举: bd_material :物料 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsource | 轻应用来源 | varchar | 2 |  | √ | ' ' | 轻应用来源,枚举: 1 :移动销售 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscm_favorites_forguser |  | forgid,fuserid,fsource,ftype |
| 2 | pk_mscm_favorites |  | fid |
